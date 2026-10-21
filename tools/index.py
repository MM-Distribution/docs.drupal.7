#!/usr/bin/env python3
"""Build md/INDEX.md: a derived table of contents for the archived docs.

The tree comes from each guide page's own child listing (its "section
contents" pane), so it matches drupal.org's hierarchy. Pages not reached that
way are listed at the end under their breadcrumb. One-line descriptions come
from each page's own meta description (og:description), cut to 140 characters.
"""
import glob
import os
import re
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "md", "INDEX.md")
ROOT = "/docs/7"

pages = {}
for f in glob.glob(os.path.join(RAW, "**", "*.html"), recursive=True):
    path = "/" + os.path.relpath(f, RAW)[:-5]
    s = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
    t = s.select_one(".pane-node-title, .pane-page-title")
    title = t.get_text(" ", strip=True) if t else path
    d = s.find("meta", property="og:description")
    desc = re.sub(r"\s+", " ", d["content"]).strip() if d and d.get("content") else ""
    if len(desc) > 140:
        desc = desc[:137].rsplit(" ", 1)[0] + "…"
    kids = []
    sc = s.select_one(".pane-section-contents")
    if sc:
        for a in sc.select("h2 a[href], h3 a[href], h4 a[href]"):
            u = urlsplit(a["href"])
            if (not u.netloc or u.netloc == "www.drupal.org") and u.path.startswith(ROOT):
                kids.append(u.path.rstrip("/"))
    crumbs = [a.get_text(" ", strip=True) for a in s.select(".breadcrumb a")]
    pages[path] = {"title": title, "desc": desc, "kids": kids, "crumbs": crumbs}

lines = []
placed = set()


def walk(path, depth):
    if path in placed or path not in pages:
        return
    placed.add(path)
    p = pages[path]
    link = os.path.relpath(os.path.join("md", path.lstrip("/") + ".md"), "md")
    lines.append(f"{'  ' * depth}- [{p['title']}]({link})" + (f" — {p['desc']}" if p["desc"] else ""))
    for k in p["kids"]:
        walk(k, depth + 1)


walk(ROOT, 0)
rest = sorted((p for p in pages if p not in placed), key=lambda p: (pages[p]["crumbs"], p))
total = len(pages)

head = [
    "# Drupal 7 documentation archive: index (derived)",
    "",
    f"{total} pages mirrored from drupal.org/docs/7 (core documentation only). Each page is "
    "`md/<url path>.md`; for example, drupal.org/docs/7/api/database-api is "
    "[`md/docs/7/api/database-api.md`](docs/7/api/database-api.md).",
    "",
    "Indented entries are children of the entry above, exactly as drupal.org's guides list "
    "them. Descriptions are the pages' own meta descriptions.",
    "",
]
body = lines
if rest:
    body = body + ["", "## Other pages", "", "Pages linked from the docs but not listed in any guide's contents.", ""]
    for p in rest:
        link = os.path.relpath(os.path.join("md", p.lstrip("/") + ".md"), "md")
        crumb = " › ".join(pages[p]["crumbs"])
        body.append(f"- [{pages[p]['title']}]({link})" + (f" — _{crumb}_" if crumb else ""))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(head + body) + "\n")
print(f"{total} pages; {len(placed)} in tree, {len(rest)} other")
