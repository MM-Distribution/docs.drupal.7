# Rules for this repo

## Considerate crawling of drupal.org (STRICT — applies to every *.drupal.org host)

These rules are mandatory for any session, agent or script that fetches from
drupal.org, www.drupal.org, api.drupal.org or any other *.drupal.org host. The
goal is to never look abusive and never get blocked. When in doubt, fetch less.

### How to fetch
- Fetch only with the WebFetch tool. The workspace shell cannot reach
  drupal.org (the egress proxy refuses it). Do not try to work around that with
  curl, wget, scripts, mirrors, caches, archive.org or a browser.
- Fetch one page at a time. No parallel fetches, and no subagents fetching
  drupal.org at the same time as each other or as the main session.

### Rate limits
- Wait at least **15 seconds** between any two requests to any *.drupal.org
  host. All hosts share one budget. robots.txt asks for `Crawl-delay: 10`; the
  extra 5 seconds is margin.
- At most **150 requests per hour** and **500 per session or day**. When you
  reach a cap, stop, save progress, and report where you stopped.

### Scope
- Fetch only documentation paths for this project: `/docs/7` and pages below
  it. Fetch other pages only if the user explicitly asks for them.
- Never fetch URLs that robots.txt disallows. These include `/search/`,
  `/admin/`, `/user/*`, `/node/add/`, `/comment/reply/`, `/book/export/*`,
  `/aggregator/*`, `/profile*`, `/project/issues/search*`, and any URL with a
  `sort=` or `solrsort=` parameter.
- Do not add query strings, follow pagination or sort links, log in, submit
  forms, or follow links off *.drupal.org.
- Re-read `https://www.drupal.org/robots.txt` once at the start of each
  crawling session, and obey it if it has changed. Its rules override this
  file wherever they are stricter.

### Never fetch the same page twice
- Keep a manifest (`crawl/manifest.tsv`: url, fetched_at, status, output_path).
  Check it before every fetch, and skip any URL already recorded with a
  successful status.
- Commit the manifest and the fetched content regularly, so an interrupted
  crawl can resume without re-fetching anything.

### Stop conditions
Stop all fetching immediately and report to the user if any of these happen:
- An HTTP 403, 429 or 503 response, a captcha, a "verify you are human" page,
  a Cloudflare-style challenge, or an access-denied page.
- Two errors or timeouts in a row.
- Content that suddenly looks empty, truncated or different from what it
  should be.

Do not retry automatically after any of these. A human decides when to resume.

### Licensing of fetched content
drupal.org documentation is © its individual contributors and licensed
**CC BY-SA 2.0**. PHP code on the site is GPL. Content copied from drupal.org
keeps that license and needs attribution: keep the source URL with every page.
The MIT `LICENSE` in this repo covers only original work in this repo, not
mirrored drupal.org text.
