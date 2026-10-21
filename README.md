# Drupal 7 documentation archive

An offline archive of the **core** Drupal 7 documentation from
[drupal.org/docs/7](https://www.drupal.org/docs/7), kept as exact copies.
Contributed-module, contributed-theme and distribution-showcase pages are left
out. Drupal 7 reached end of life on January 5, 2025.

**Start at [`md/INDEX.md`](md/INDEX.md).**

## What's here

| Path | What it is |
|---|---|
| `raw/` | Every page exactly as drupal.org served it: the full HTML response, byte for byte. This is the archival original. |
| `md/` | The same pages as markdown, for fast reading by people and LLMs. One file per page at `md/<url path>.md`. |
| `md/INDEX.md` | Table of contents in drupal.org's own guide order, with each page's description (derived). |
| `notes/` | Our own notes and examples, kept apart from the copies (MIT). |
| `crawl/` | Crawl manifest (every request, when, status, file), robots.txt copy, exclusion list. |
| `tools/` | The crawler, HTML-to-markdown converter and index builder. |

## How exact is the markdown?

Each `md/` page contains the page title, the article body and, on guide pages,
the listing of child pages. These are converted from `raw/` by
[pandoc](https://pandoc.org) with no wrapping, so no text is added, removed or
reworded. The only changes are markup:

- layout wrappers (`div`, `span`, `section`) are unwrapped, keeping their contents
- empty permalink anchors next to headings are dropped
- `rel`, `class` and `target` attributes on links, and sizing attributes on
  images, are dropped
- code blocks are labelled with their language (from the page's own
  `language-php`-style class)
- runs of spaces collapse to one, as they do when the HTML is displayed

Site chrome is left out: navigation, sidebars, ads, the Drupal 7 end-of-life
notice, the "help improve this page" box, comments and the footer. Front matter
at the top of each file holds the source URL, the "Last updated" line, dates
and a pointer to the raw file.

Links are kept exactly as written. A root-relative link like
`/docs/7/api/database-api` refers to `md/docs/7/api/database-api.md`. Images
still point at drupal.org; they are not archived.

## Crawling

`tools/crawl.py` is the only way this repo fetches drupal.org. It enforces
the rules in [`CLAUDE.md`](CLAUDE.md): one request at a time, at least 15
seconds apart, at most 150 an hour and 500 a day, obeying robots.txt, and it
never refetches a saved page. It stops for good on any 403, 429 or 5xx
response or bot challenge, until a person reviews it and deletes
`crawl/STOPPED`.

```sh
tools/crawl.py            # resume the crawl (picks up where it left off)
tools/convert.py          # rebuild md/ from raw/
tools/index.py            # rebuild md/INDEX.md
```

This needs `python3` with BeautifulSoup, plus `pandoc` and `curl`.

## License

- `raw/` and `md/` are drupal.org documentation, © 2000–2026 its individual
  contributors, licensed **CC BY-SA 2.0**. See [`LICENSE`](LICENSE). Each page
  keeps its source URL for attribution. Code samples in the docs are GPL.
- `tools/` and `notes/` are original work under the **MIT** license. See
  [`LICENSE-MIT`](LICENSE-MIT).

Drupal is a registered trademark of Dries Buytaert. This archive is not
affiliated with or endorsed by the Drupal Association.
