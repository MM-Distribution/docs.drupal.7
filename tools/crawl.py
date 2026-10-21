#!/usr/bin/env python3
"""Considerate crawler for the Drupal 7 docs on drupal.org.

Enforces the rules in CLAUDE.md in code:
- one request at a time, never two crawler copies at once (lock file)
- at least 15 s between requests, persisted across runs (crawl/.last_fetch)
- at most 150 requests per rolling hour and 500 per rolling 24 h
  (crawl/.request_log)
- robots.txt re-read at the start of every run and obeyed
- scope: www.drupal.org/docs/7 and below, minus crawl/exclude.txt prefixes;
  no query strings
- never re-fetches a URL already saved with status 200 (crawl/manifest.tsv)
- stop conditions write crawl/STOPPED and the crawler then refuses to run
  until a human deletes that file

Each response body is saved exactly as received to raw/<url path>.html.

Usage: tools/crawl.py [--max N] [--commit-every N]
"""
import argparse
import fcntl
import os
import re
import subprocess
import sys
import time
import urllib.robotparser
from datetime import datetime, timezone
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup

HOST = "www.drupal.org"
ROOT_PATH = "/docs/7"
SEEDS = [f"https://{HOST}{ROOT_PATH}"]
UA = "mm-distribution-docs-archiver/1.0 (+https://github.com/mm-distribution)"
DELAY = 15
HOURLY_CAP = 150
DAILY_CAP = 500
TIMEOUT = 60

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAWL = os.path.join(REPO, "crawl")
RAW = os.path.join(REPO, "raw")
MANIFEST = os.path.join(CRAWL, "manifest.tsv")
LAST = os.path.join(CRAWL, ".last_fetch")
LOG = os.path.join(CRAWL, ".request_log")
LOCK = os.path.join(CRAWL, ".lock")
STOPPED = os.path.join(CRAWL, "STOPPED")
EXCLUDE = os.path.join(CRAWL, "exclude.txt")
ROBOTS_COPY = os.path.join(CRAWL, "robots.txt")

CHALLENGE = re.compile(r"captcha|verify you are human|just a moment\.\.\.|cf-challenge|"
                       r"challenge-platform|access denied|attention required", re.I)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    print(f"[{now_iso()}] {msg}", flush=True)


def stop(reason):
    with open(STOPPED, "w") as f:
        f.write(f"{now_iso()} {reason}\n")
    log(f"STOPPED: {reason}")
    sys.exit(2)


# ------------------------------------------------------------- rate limiting
def read_log():
    try:
        return [float(x) for x in open(LOG).read().split()]
    except FileNotFoundError:
        return []


def wait_turn():
    """Block until the next request is allowed; exit if a cap is reached."""
    t = time.time()
    stamps = [s for s in read_log() if t - s < 86400]
    if len(stamps) >= DAILY_CAP:
        log(f"Daily cap of {DAILY_CAP} requests reached; stopping this run.")
        sys.exit(0)
    hour = [s for s in stamps if t - s < 3600]
    if len(hour) >= HOURLY_CAP:
        resume = min(hour) + 3600
        log(f"Hourly cap reached; waiting {int(resume - t)} s.")
        time.sleep(max(0, resume - t) + 1)
    try:
        last = float(open(LAST).read().strip())
    except (FileNotFoundError, ValueError):
        last = 0
    gap = DELAY - (time.time() - last)
    if gap > 0:
        time.sleep(gap)


def record_request():
    t = time.time()
    with open(LAST, "w") as f:
        f.write(f"{int(t)}\n")
    stamps = [s for s in read_log() if t - s < 86400] + [t]
    with open(LOG, "w") as f:
        f.write("\n".join(f"{s:.0f}" for s in stamps) + "\n")


def fetch(url):
    """One HTTP GET via curl (goes through the workspace proxy). No redirects followed."""
    wait_turn()
    out = os.path.join(CRAWL, ".body.tmp")
    cmd = ["curl", "-sS", "--compressed", "--max-time", str(TIMEOUT), "-A", UA,
           "-H", "Accept: text/html", "-o", out,
           "-w", "%{http_code}\t%{redirect_url}\t%{content_type}", url]
    record_request()
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        return None, None, None, p.stderr.strip()
    code, redirect, ctype = (p.stdout.split("\t") + ["", ""])[:3]
    body = open(out, "rb").read() if os.path.exists(out) else b""
    return int(code), redirect, body, ctype


# ------------------------------------------------------------------- scope
def load_excludes():
    if not os.path.exists(EXCLUDE):
        return []
    return [l.strip().rstrip("/") for l in open(EXCLUDE) if l.strip() and not l.startswith("#")]


def normalize(href, base):
    if not href or href.startswith(("mailto:", "javascript:", "#")):
        return None
    u = urlsplit(urljoin(base, href))
    if u.scheme not in ("http", "https") or u.netloc != HOST or u.query:
        return None
    path = re.sub(r"/+$", "", u.path) or "/"
    return f"https://{HOST}{path}"


def in_scope(url, rp, excludes):
    path = urlsplit(url).path
    if not (path == ROOT_PATH or path.startswith(ROOT_PATH + "/")):
        return False
    for ex in excludes:
        if path == ex or path.startswith(ex + "/"):
            return False
    return rp.can_fetch(UA, url) and rp.can_fetch("*", url)


def raw_path(url):
    return os.path.join(RAW, urlsplit(url).path.lstrip("/") + ".html")


# ----------------------------------------------------------------- parsing
SKIP_PANES = ("carbon-ad", "help-improve", "pane-node-links", "table-of-contents")


def doc_links(html, base):
    """Links from the documentation node: body, guide menu, child listings."""
    s = BeautifulSoup(html, "html.parser")
    node = s.select_one(".node-documentation") or s.select_one("#block-system-main") or s
    for pane in node.select(".panel-pane"):
        if any(k in " ".join(pane.get("class", [])) for k in SKIP_PANES):
            pane.decompose()
    links = []
    for a in node.find_all("a", href=True):
        u = normalize(a["href"], base)
        if u:
            links.append(u)
    return links


def looks_like_doc(html):
    s = BeautifulSoup(html, "html.parser")
    return bool(s.select_one(".node-documentation") or s.select_one(".pane-node-title")
                or s.select_one("#block-system-main"))


# ---------------------------------------------------------------- manifest
def load_manifest():
    done, rows = {}, []
    if os.path.exists(MANIFEST):
        for line in open(MANIFEST).read().splitlines()[1:]:
            parts = line.split("\t")
            if len(parts) >= 3:
                rows.append(parts)
                done[parts[0]] = parts[2]
    return done


def append_manifest(url, status, path):
    new = not os.path.exists(MANIFEST)
    with open(MANIFEST, "a") as f:
        if new:
            f.write("url\tfetched_at\tstatus\toutput_path\n")
        f.write(f"{url}\t{now_iso()}\t{status}\t{path}\n")


def git_commit(msg):
    subprocess.run(["git", "-C", REPO, "add", "raw", "crawl"], check=False)
    r = subprocess.run(["git", "-C", REPO, "-c", "user.name=Phil", "-c", "user.email=philsward@mm-distribution.com",
                        "commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
                        "Claude-Session: https://claude.ai/code/session_01EvP8SahjqYcYBiDCoNmZFe"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        subprocess.run(["git", "-C", REPO, "push", "-q", "origin", "HEAD:main"], check=False)


# -------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=DAILY_CAP, help="max page requests this run")
    ap.add_argument("--commit-every", type=int, default=25)
    args = ap.parse_args()

    if os.path.exists(STOPPED):
        print(f"Refusing to run: {STOPPED} exists:\n{open(STOPPED).read()}A human must review and delete it.")
        sys.exit(2)
    lock = open(LOCK, "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("Another crawler is running.")
        sys.exit(2)

    # Re-read robots.txt at the start of every run.
    code, _, body, info = fetch(f"https://{HOST}/robots.txt")
    if code != 200:
        stop(f"robots.txt returned {code} {info}")
    text = body.decode("utf-8", "replace")
    with open(ROBOTS_COPY, "w") as f:
        f.write(text)
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(text.splitlines())
    cd = rp.crawl_delay("*")
    if cd and cd > DELAY:
        stop(f"robots.txt Crawl-delay is now {cd}s, above our {DELAY}s; update the crawler first")
    excludes = load_excludes()
    log(f"robots.txt ok (crawl-delay {cd}); {len(excludes)} excluded prefixes")

    done = load_manifest()
    # Rebuild the frontier from everything already saved, so runs resume cleanly.
    queue, seen = [], set()

    def enqueue(u):
        if u and u not in seen and in_scope(u, rp, excludes):
            seen.add(u)
            if done.get(u, "").split(" ")[0] not in ("200", "301", "302", "404", "410"):
                queue.append(u)

    for s_ in SEEDS:
        enqueue(s_)
    for url, status in list(done.items()):
        rp_ = raw_path(url)
        if status.startswith("200") and os.path.exists(rp_):
            for u in doc_links(open(rp_, encoding="utf-8", errors="replace").read(), url):
                enqueue(u)
    log(f"{sum(1 for v in done.values() if v.startswith('200'))} pages already saved; {len(queue)} queued")

    fetched = errors = since_commit = 0
    while queue and fetched < args.max:
        url = queue.pop(0)
        code, redirect, body, info = fetch(url)
        fetched += 1
        if code is None:
            errors += 1
            append_manifest(url, f"error {info}"[:200], "-")
            log(f"ERROR {url}: {info}")
            if errors >= 2:
                stop(f"two errors in a row; last: {url} {info}")
            continue
        if code in (403, 429) or code >= 500:
            append_manifest(url, str(code), "-")
            stop(f"HTTP {code} for {url}")
        if code in (301, 302, 303, 307, 308):
            errors = 0
            append_manifest(url, f"{code} -> {redirect}", "-")
            target = normalize(redirect, url)
            log(f"{code} {url} -> {redirect}")
            enqueue(target)
            continue
        if code in (404, 410):
            errors = 0
            append_manifest(url, str(code), "-")
            log(f"{code} {url}")
            continue
        if code != 200:
            append_manifest(url, str(code), "-")
            stop(f"unexpected HTTP {code} for {url}")
        html = body.decode("utf-8", "replace")
        if len(body) < 2000 or not looks_like_doc(html):
            append_manifest(url, "200 unexpected-content", "-")
            if CHALLENGE.search(html):
                stop(f"bot challenge or access-denied page at {url}")
            stop(f"page does not look like a docs page ({len(body)} bytes) at {url}")
        errors = 0
        out = raw_path(url)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(body)
        rel = os.path.relpath(out, REPO)
        append_manifest(url, "200", rel)
        new = 0
        for u in doc_links(html, url):
            before = len(queue)
            enqueue(u)
            new += len(queue) - before
        log(f"200 {url} ({len(body)} B, +{new} new, {len(queue)} queued)")
        since_commit += 1
        if args.commit_every and since_commit >= args.commit_every:
            git_commit(f"Crawl: save {since_commit} more docs pages")
            since_commit = 0

    if since_commit:
        git_commit(f"Crawl: save {since_commit} more docs pages")
    log(f"Run finished: {fetched} requests; {len(queue)} still queued")


if __name__ == "__main__":
    main()
