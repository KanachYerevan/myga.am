#!/usr/bin/env python3
"""Analyse the cached Search Console and GA4 data and write a Markdown report.

Usage:
    python bin/seo/analyze.py
"""

import re
from collections import defaultdict
from datetime import date
from urllib.parse import urlparse

from _auth import ROOT, log, read_cache

REPORT_DIR = ROOT / "docs" / "reports"
LANG_PREFIXES = {"ru": "ru", "hy": "hy"}

# Rough CTR-by-position curve used to flag pages that under-perform their rank.
CTR_CURVE = [
    (1, 0.30),
    (2, 0.16),
    (3, 0.10),
    (4, 0.07),
    (5, 0.05),
    (6, 0.04),
    (10, 0.025),
    (20, 0.012),
]

ARMENIAN = re.compile(r"[\u0530-\u058F]")
CYRILLIC = re.compile(r"[\u0400-\u04FF]")

BRAND_TERMS = ["kanach", "yerevan", "kanachyerevan", "կանաչ", "երևան", "երեւան", "ереван"]


def expected_ctr(position):
    for max_pos, ctr in CTR_CURVE:
        if position <= max_pos:
            return ctr
    return 0.005


def is_brand(query):
    lowered = query.lower()
    return any(term in lowered for term in BRAND_TERMS)


def script_of(text):
    if ARMENIAN.search(text):
        return "armenian"
    if CYRILLIC.search(text):
        return "russian"
    return "latin"


def url_path(url):
    """Return only the path component, whether given a full URL or a path."""
    return urlparse(url).path or "/"


def url_lang(path):
    stripped = url_path(path).lstrip("/")
    first = stripped.split("/", 1)[0].lower()
    if first in LANG_PREFIXES:
        return LANG_PREFIXES[first]
    return "en"


def url_to_file(path):
    """Best-effort map from a live URL path to a source Markdown file."""
    stripped = url_path(path).strip("/")
    if not stripped:
        return None
    segments = stripped.split("/")
    lang = "en"
    if segments[0].lower() in LANG_PREFIXES:
        lang = segments[0].lower()
        segments = segments[1:]
    slug = "/".join(segments)
    if not slug:
        return None
    candidates = []
    if lang == "en":
        candidates += [f"content/{slug}/index.md", f"content/{slug}.md"]
    else:
        candidates += [
            f"content/{slug}/index.{lang}.md",
            f"content/{slug}.{lang}.md",
        ]
    candidates += [f"content/{slug}/index.md", f"content/{slug}.md"]
    for candidate in candidates:
        if (ROOT / candidate).exists():
            return candidate
    return None


def window(gsc, name):
    return gsc.get("windows", {}).get(name, {}).get("data", {})


def ga4_window(ga4, name):
    return ga4.get("windows", {}).get(name, {}).get("data", {})


def as_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def monthly_trend(daily):
    months = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0})
    for row in daily:
        month = row["date"][:7]
        months[month]["clicks"] += as_float(row["clicks"])
        months[month]["impressions"] += as_float(row["impressions"])
    return dict(sorted(months.items()))


def main():
    gsc = read_cache("gsc.json")
    ga4 = read_cache("ga4.json")

    m16 = window(gsc, "16m")
    d90 = window(gsc, "90d")
    queries = d90.get("queries", [])
    pages = d90.get("pages", [])
    query_page = d90.get("query_page", [])

    totals_clicks = sum(as_float(r["clicks"]) for r in m16.get("pages", []))
    totals_impr = sum(as_float(r["impressions"]) for r in m16.get("pages", []))

    # --- Opportunities -----------------------------------------------------
    striking = sorted(
        [
            r
            for r in queries
            if 4 <= as_float(r["position"]) <= 20 and as_float(r["impressions"]) >= 20
        ],
        key=lambda r: as_float(r["impressions"]),
        reverse=True,
    )[:25]

    ctr_gaps = []
    for row in pages:
        impressions = as_float(row["impressions"])
        if impressions < 100:
            continue
        gap = expected_ctr(as_float(row["position"])) - as_float(row["ctr"])
        if gap > 0.02:
            ctr_gaps.append((gap * impressions, gap, row))
    ctr_gaps.sort(key=lambda item: item[0], reverse=True)

    by_query = defaultdict(list)
    for row in query_page:
        by_query[row["query"]].append(row)

    best_page_by_query = {}
    for query, rows in by_query.items():
        best_page_by_query[query] = max(rows, key=lambda r: as_float(r["impressions"]))
    cannibal = [
        (query, rows)
        for query, rows in by_query.items()
        if len(rows) >= 2 and sum(as_float(r["impressions"]) for r in rows) >= 50
    ]
    cannibal.sort(
        key=lambda item: sum(as_float(r["impressions"]) for r in item[1]), reverse=True
    )

    # --- Per-language ------------------------------------------------------
    lang_stats = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0, "rows": 0})
    for row in pages:
        stats = lang_stats[url_lang(row["page"])]
        stats["clicks"] += as_float(row["clicks"])
        stats["impressions"] += as_float(row["impressions"])
        stats["rows"] += 1

    query_lang = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0, "n": 0})
    for row in queries:
        stats = query_lang[script_of(row["query"])]
        stats["clicks"] += as_float(row["clicks"])
        stats["impressions"] += as_float(row["impressions"])
        stats["n"] += 1

    brand = {"clicks": 0.0, "impressions": 0.0}
    nonbrand = {"clicks": 0.0, "impressions": 0.0}
    for row in queries:
        target = brand if is_brand(row["query"]) else nonbrand
        target["clicks"] += as_float(row["clicks"])
        target["impressions"] += as_float(row["impressions"])

    # --- GA4 ---------------------------------------------------------------
    ga4_365 = ga4_window(ga4, "365d")
    ga4_90 = ga4_window(ga4, "90d")
    channels = {r["sessionDefaultChannelGroup"]: r for r in ga4_365.get("channel", [])}
    organic = channels.get("Organic Search", {})
    organic_sessions = as_float(organic.get("sessions"))
    gsc_clicks_16m = totals_clicks

    ga4_langs = ga4_365.get("language", [])
    landing = [
        r
        for r in ga4_90.get("landing", [])
        if r.get("sessionDefaultChannelGroup") == "Organic Search"
    ]
    landing.sort(key=lambda r: as_float(r["sessions"]), reverse=True)

    # --- Render ------------------------------------------------------------
    today = date.today()
    lines = []
    add = lines.append

    month_label = today.strftime("%B %Y")
    add("---")
    add(f'title: "SEO Report — {month_label}"')
    add(
        'summary: "Search Console and GA4 analysis for kanachyerevan.am with prioritised, '
        'file-level recommendations to improve search visibility."'
    )
    add(f"date: {today.isoformat()}")
    add("---")
    add("")
    add(f"# SEO Report — {month_label}")
    add("")
    add(f"- GSC property: `{gsc.get('site')}`")
    add(f"- GA4 property: `{ga4.get('property_id')}`")
    add(f"- Reporting window: last 90 days for opportunities, 16 months for totals.")
    add("")

    add("## Executive summary")
    add("")
    add(f"- 16-month totals: **{int(gsc_clicks_16m):,} clicks** from **{int(totals_impr):,} impressions**.")
    add(f"- Organic search sessions (GA4, 365 days): **{int(organic_sessions):,}**.")
    add(
        f"- Brand vs non-brand (90 days): brand {int(brand['clicks']):,} clicks / "
        f"{int(brand['impressions']):,} impressions; non-brand "
        f"{int(nonbrand['clicks']):,} clicks / {int(nonbrand['impressions']):,} impressions."
    )
    add(f"- Striking-distance queries identified: **{len(striking)}**.")
    add(f"- Pages under-performing their rank (CTR gap): **{len(ctr_gaps)}**.")
    add(f"- Cannibalisation cases: **{len(cannibal)}**.")
    add("")

    add("## Striking-distance queries (position 4–20, ≥20 impressions)")
    add("")
    add("Moving these to the top 3 has the highest expected click gain.")
    add("")
    add("| Query | Clicks | Impressions | CTR | Position | Ranking page | Target file |")
    add("| --- | ---: | ---: | ---: | ---: | --- | --- |")
    for row in striking:
        best = best_page_by_query.get(row["query"])
        page = best["page"] if best else "—"
        source = (url_to_file(page) if best else None) or "—"
        add(
            f"| {row['query']} | {int(as_float(row['clicks']))} | "
            f"{int(as_float(row['impressions']))} | {as_float(row['ctr'])*100:.1f}% | "
            f"{as_float(row['position']):.1f} | {page} | {source} |"
        )
    add("")

    add("## CTR opportunities (high impressions, weak CTR for their rank)")
    add("")
    add("| Page | File | Impressions | CTR | Position | Expected CTR | Gap |")
    add("| --- | --- | ---: | ---: | ---: | ---: | ---: |")
    for _, gap, row in ctr_gaps[:20]:
        source = url_to_file(row["page"]) or "—"
        add(
            f"| {row['page']} | {source} | {int(as_float(row['impressions']))} | "
            f"{as_float(row['ctr'])*100:.1f}% | {as_float(row['position']):.1f} | "
            f"{expected_ctr(as_float(row['position']))*100:.1f}% | {gap*100:.1f} pp |"
        )
    add("")

    add("## Cannibalisation (query ranked by several pages)")
    add("")
    for query, rows in cannibal[:15]:
        add(f"**{query}** — {len(rows)} pages")
        add("")
        for row in sorted(rows, key=lambda r: as_float(r["impressions"]), reverse=True):
            add(
                f"- {row['page']} — {int(as_float(row['clicks']))} clicks, "
                f"{int(as_float(row['impressions']))} impressions, "
                f"position {as_float(row['position']):.1f}"
            )
        add("")

    add("## Per-language performance (90 days)")
    add("")
    add("| Language | Landing pages | Clicks | Impressions |")
    add("| --- | ---: | ---: | ---: |")
    for lang, stats in sorted(lang_stats.items()):
        add(
            f"| {lang} | {stats['rows']} | {int(stats['clicks'])} | "
            f"{int(stats['impressions'])} |"
        )
    add("")
    add("Query language mix (by script):")
    add("")
    add("| Script | Queries | Clicks | Impressions |")
    add("| --- | ---: | ---: | ---: |")
    for lang, stats in sorted(query_lang.items()):
        add(
            f"| {lang} | {stats['n']} | {int(stats['clicks'])} | "
            f"{int(stats['impressions'])} |"
        )
    add("")

    add("## GA4 — language and engagement (365 days)")
    add("")
    add("| Language | Sessions | Users | Engagement rate |")
    add("| --- | ---: | ---: | ---: |")
    for row in sorted(ga4_langs, key=lambda r: as_float(r["sessions"]), reverse=True)[:10]:
        add(
            f"| {row.get('language')} | {int(as_float(row.get('sessions')))} | "
            f"{int(as_float(row.get('totalUsers')))} | "
            f"{as_float(row.get('engagementRate'))*100:.1f}% |"
        )
    add("")

    add("## GA4 — top organic landing pages (90 days)")
    add("")
    add("| Landing page | Sessions | Engagement rate | Target file |")
    add("| --- | ---: | ---: | --- |")
    for row in landing[:20]:
        page = row.get("landingPagePlusQueryString", "")
        source = url_to_file(page.split("?")[0]) or "—"
        add(
            f"| {page} | {int(as_float(row.get('sessions')))} | "
            f"{as_float(row.get('engagementRate'))*100:.1f}% | {source} |"
        )
    add("")

    add("## Technical SEO status")
    add("")
    add("Applied in this repository:")
    add("")
    add("- **Canonical tags** added for every page and section (`partials/seo.html`).")
    add("- **hreflang + x-default** added for `en` / `ru` / `hy` across all translations.")
    add("- **Meta descriptions** resolved via `page.description` → `page.summary` → "
        "auto excerpt from rendered content (`partials/page-cards.html`).")
    add("- **Open Graph / Twitter cards** now emit type, title, description, URL and image.")
    add("- **JSON-LD**: `Organization` on every page, `Article` on dated pages "
        "(`partials/structured-data.html`).")
    add("- **sitemap.xml / robots.txt** are generated by Zola; confirm both are submitted "
        "and crawlable in Search Console.")
    add("")
    add("Remaining, editorial (not automatable):")
    add("")
    add("- Add a hand-written `description` to important pages — auto excerpts are a "
        "fallback, not a substitute.")
    add("- Fix cannibalisation by consolidating or cross-linking competing pages.")
    add("")

    add("## Search vs analytics reconciliation")
    add("")
    add(f"- GSC clicks (16 months): **{int(gsc_clicks_16m):,}**")
    add(f"- GA4 organic search sessions (365 days): **{int(organic_sessions):,}**")
    add("- A large gap usually means: consent/blocking, tag not firing on all pages, "
        "brand queries landing on pages without the tag, or GA4 attribution differences.")
    add("")

    add("## Monthly trend (GSC, 16 months)")
    add("")
    add("| Month | Clicks | Impressions |")
    add("| --- | ---: | ---: |")
    for month, stats in monthly_trend(m16.get("daily", [])).items():
        add(f"| {month} | {int(stats['clicks'])} | {int(stats['impressions'])} |")
    add("")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"seo-{today.strftime('%Y-%m')}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"Wrote {path}")


if __name__ == "__main__":
    main()
