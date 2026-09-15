---
title: Search Analytics Pipeline
summary: "How to run the Search Console and GA4 analysis pipeline, where credentials live, and how to read the generated report."
---

# Search Analytics Pipeline

This project pulls Google Search Console and Google Analytics 4 data through a
read-only service account, analyses it, and writes a prioritised report to
`docs/reports/`.

## Credentials

- Key file: `.secrets/ga4-sa.json` (gitignored — never commit it).
- Service account: `opencode@gen-lang-client-0891408543.iam.gserviceaccount.com`.
- It must be added as **Viewer** in GA4 and as a read user in Search Console.
- Override defaults with environment variables:
  - `GOOGLE_APPLICATION_CREDENTIALS` — path to the JSON key.
  - `GA4_PROPERTY_ID` — defaults to `475759852`.
  - `GSC_SITE` — defaults to `sc-domain:kanachyerevan.am`.

## Running

```bash
make seo
```

This runs, in order:

1. `bin/seo/gsc_report.py` — Search Console queries, pages, query×page, daily and
   country/device dimensions for the 90-day, 180-day and 16-month windows. Cached
   to `data/seo-cache/gsc.json`.
2. `bin/seo/ga4_report.py` — GA4 channels, landing pages, pages, language, country,
   device and source/medium for the 90-day and 365-day windows. Cached to
   `data/seo-cache/ga4.json`.
3. `bin/seo/analyze.py` — reads the caches and writes `docs/reports/seo-YYYY-MM.md`.

The cache files are gitignored; only the report is committed.

## Reading the report

- **Striking-distance queries** — ranking 4–20 with real demand; the best short-term
  win.
- **CTR opportunities** — pages that rank well but earn few clicks, usually a title
  or description problem.
- **Cannibalisation** — one query served by several pages; consolidate or cross-link.
- **Per-language performance** — how English, Russian and Armenian search differ.
- **Technical SEO status** — what the templates already emit and what still needs
  hand-written editorial work.

## Setup (one-time, from scratch)

```bash
python3 -m venv .venv
.venv/bin/pip install google-analytics-data google-api-python-client google-auth
```

## Notes

- Search Console retains roughly 16 months of data; GA4 keeps about 14.
- The service account is read-only and can be revoked at any time.
