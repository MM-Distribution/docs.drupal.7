#!/usr/bin/env python3
"""Convert saved drupal.org docs pages (raw/**/*.html) into markdown (md/**/*.md).

Deterministic: the article HTML is cut out of the saved page and converted by
pandoc (html -> gfm, no line wrapping). No text is added, removed or reworded.
What is kept from each page:
- the page title (as the H1)
- the article body
- on guide pages, the "section contents" listing of child pages
Everything else on the page (site navigation, sidebars, ads, the Drupal 7
end-of-life notice, "help improve this page" box, comments, footer) is left out.
Metadata goes in YAML front matter, separate from the copied text.

Links and image URLs are kept exactly as written in the original HTML, so
root-relative links like /docs/7/foo stay as they are. The page for
/docs/7/foo is md/docs/7/foo.md.

Usage: tools/convert.py [raw-file ...]   (default: every file under raw/)
"""
import glob
import json
import os
import subprocess
import sys

from bs4 import BeautifulSoup

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, "raw")
MD = os.path.join(REPO, "md")
MANIFEST = os.path.join(REPO, "crawl", "manifest.tsv")
HOST = "https://www.drupal.org"


def clean(fragment):
    """Remove markup-only noise before conversion; text and code are untouched.

    - empty permalink/name anchors (<a class="toc-anchor">, <a name="x"></a>)
    - layout wrappers: <div> and <span> tags are unwrapped (their contents stay)
    """
    frag = BeautifulSoup(fragment, "html.parser")
    for a in frag.find_all("a"):
        if not a.get_text(strip=True) and not a.find("img") and (
                "toc-anchor" in a.get("class", []) or a.get("name") or (a.get("id") and not a.get("href"))):
            a.decompose()
    # Code blocks: label the fence with the language from <code class="language-x">.
    for pre in frag.find_all("pre"):
        code = pre.find("code")
        langs = [c[9:] for c in (code.get("class", []) if code else []) if c.startswith("language-")]
        pre.attrs = {"class": langs[:1]} if langs else {}
        if code:
            code.attrs = {}
    # Presentation-only attributes that force raw HTML in markdown output.
    for a in frag.find_all("a"):
        for attr in ("rel", "class", "target"):
            a.attrs.pop(attr, None)
    for img in frag.find_all("img"):
        for attr in ("class", "style", "width", "height", "typeof", "loading"):
            img.attrs.pop(attr, None)
    for tag in frag.find_all(["div", "span", "section", "article", "header", "footer"]):
        if tag.find_parent(["pre", "code"]):
            continue
        tag.unwrap()
    return str(frag)


def pandoc(html):
    p = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
                       input=html, capture_output=True, text=True, check=True)
    return p.stdout.strip()


def yaml_str(s):
    return json.dumps(s, ensure_ascii=False)


def fetched_dates():
    out = {}
    if os.path.exists(MANIFEST):
        for line in open(MANIFEST).read().splitlines()[1:]:
            p = line.split("\t")
            if len(p) >= 4 and p[2] == "200":
                out[p[3]] = p[1]
    return out


def convert(raw_file, fetched):
    rel = os.path.relpath(raw_file, RAW)
    url_path = "/" + rel[:-len(".html")]
    html = open(raw_file, encoding="utf-8").read()
    s = BeautifulSoup(html, "html.parser")
    main = s.select_one("#block-system-main") or s

    t = main.select_one(".pane-node-title, .pane-page-title")
    title = t.get_text(" ", strip=True) if t else (s.title.string.split(" | ")[0] if s.title else url_path)
    upd = main.select_one(".pane-node-updated")
    updated = upd.get_text(" ", strip=True) if upd else None

    body = main.select_one(".pane-node-body .field-name-body") or main.select_one(".pane-node-body")
    body_html = body.decode_contents() if body else ""
    contents = main.select_one(".pane-section-contents")
    contents_html = contents.decode_contents() if contents else ""

    crumbs = [a.get_text(" ", strip=True) for a in s.select(".breadcrumb a, nav.breadcrumb a")]
    meta = {m.get("property"): m.get("content") for m in s.find_all("meta") if m.get("property")}
    body_classes = s.body.get("class", []) if s.body else []
    kind = "guide" if "node-type-guide" in body_classes else "page"

    fm = ["---",
          f"title: {yaml_str(title)}",
          f"source_url: {yaml_str(HOST + url_path)}",
          f"page_type: {kind}"]
    if updated:
        fm.append(f"last_updated: {yaml_str(updated)}")
    for k, name in (("article:published_time", "published"), ("article:modified_time", "modified")):
        if meta.get(k):
            fm.append(f"{name}: {yaml_str(meta[k])}")
    if crumbs:
        fm.append("breadcrumb: [" + ", ".join(yaml_str(c) for c in crumbs) + "]")
    if os.path.relpath(raw_file, REPO) in fetched:
        fm.append(f"fetched: {yaml_str(fetched[os.path.relpath(raw_file, REPO)])}")
    fm.append(f"raw: {yaml_str(os.path.relpath(raw_file, REPO))}")
    fm.append('license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"')
    fm.append("---")

    parts = ["\n".join(fm), f"# {title}"]
    if body_html.strip():
        parts.append(pandoc(clean(body_html)))
    if contents_html.strip():
        parts.append(pandoc(clean(contents_html)))
    out = os.path.join(MD, rel[:-len(".html")] + ".md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n\n".join(p for p in parts if p).rstrip() + "\n")
    return out, title, kind


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(RAW, "**", "*.html"), recursive=True))
    fetched = fetched_dates()
    for f in files:
        out, title, kind = convert(f, fetched)
        print(f"{kind}\t{os.path.relpath(out, REPO)}\t{title}")


if __name__ == "__main__":
    main()
