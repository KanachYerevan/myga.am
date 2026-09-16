---
title: "SEO Action Plan — September 2026"
summary: "Problem inventory and prioritised action items derived from the September 2026 Search Console and GA4 report, with proposed titles, file targets and a 90-day measurement plan."
date: 2026-09-15
---

# SEO Action Plan — September 2026

This plan turns the data in [the September report](seo-2026-09.md) into concrete
problems and actions. Evidence windows: Search Console last 90 days (opportunities)
and 16 months (totals); GA4 last 90 and 365 days.

## 1. Situation snapshot

| Metric                                           |                     Value |
| ------------------------------------------------ | ------------------------: |
| Clicks (16 months)                               |                       303 |
| Impressions (16 months)                          |                     9,469 |
| Blended CTR                                      |                      3.2% |
| GSC clicks, last 90 days                         | 222 (en 88, ru 90, hy 44) |
| GA4 organic sessions (365 days)                  |                       548 |
| GA4 direct sessions (365 days)                   |                     2,164 |
| Pages ranking position 4–20 with ≥20 impressions |                 9 queries |

The site is **visible but not clickable**: many pages rank between positions 4 and 9
yet earn almost no clicks. That is a snippet/intent problem, not a ranking problem,
and it is the cheapest thing to fix.

## 2. Problems detected

### P1 — Good positions, near-zero CTR (highest impact)

| Query                                 | Impressions | Clicks |  CTR | Position |
| ------------------------------------- | ----------: | -----: | ---: | -------: |
| `kanach`                              |         377 |      1 | 0.3% |      5.6 |
| `ակտիվ քաղաքացի հարթակ`               |         376 |      1 | 0.3% |      6.3 |
| `european tree pruning standard`      |          70 |      0 | 0.0% |      8.3 |
| `հհ անտառային օրենսգիրք`              |          62 |      0 | 0.0% |      9.0 |
| `синица`                              |          42 |      0 | 0.0% |      7.4 |
| `law on plant world` (RU/EN variants) |          19 |      0 | 0.0% |      8.2 |

**Root cause:** titles are bare or generic, and several pages have no compelling
description. People see the result and choose a competitor.

### P2 — Home page title is not optimised or localised

- `/` title is only `Kanach Yerevan` (14 characters); H1 is the same.
- `/ru/` uses the **English** title `Kanach Yerevan` even though the page is Russian.
- The query `kanach` is split across five URLs (`/`, `/ru/`, `/about/`,
  `/ru/about/`, `/hy/`) — 377 impressions, 1 click.

**Root cause:** the home template prints `section.title` verbatim and there is no
separate SEO title field, so the brand name doubles as the H1 and the `<title>`.

### P3 — Intent mismatch on the Active Citizen case page

`ակտիվ քաղաքացի հարթակ` (376 impressions) lands on
`/hy/status/cases/active-citizen/`, a page about one rejection, not about the
platform itself. The title is 67 characters and gets truncated.

**Root cause:** the highest-demand Armenian query has no page that answers it.

### P4 — A PDF competes with its own HTML page

- `/guidelines/legal/eac-pruning/` — 279 impressions, 2 clicks, position 6.5.
- `/documents/European%20Tree%20Pruning%20Standard%202021-RU.pdf` — 261 impressions,
  6 clicks, position 8.4.

The HTML page is thin (a heading and download links), so Google often prefers the
PDF. A PDF cannot convert visitors into readers, reports or members.

### P5 — Duplicate content between Journal and Guidelines/Legal

| Journal page                      | Guidelines/Legal page                            | Issue                    |
| --------------------------------- | ------------------------------------------------ | ------------------------ |
| `/journal/tree-valuation-reform/` | `/guidelines/legal/draft-valuation/`             | near-identical titles    |
| `/hy/status/participation/`       | `/hy/guidelines/legal/proactive-greening-draft/` | identical Armenian title |

Two pages compete for the same intent. Google picks one, and the other dilutes it.

### P6 — Legal pages rank broadly but earn no clicks

`gcap` (142 imp, 0 clicks), `elders-green-spaces` (133 imp, 2 clicks),
`law-on-plant-world` (133 imp, 2 clicks), `forest-code` (128 imp, 1 click). These
are useful reference pages with no "so what" summary in the snippet.

### P7 — 21 section pages have no meta description

After the template fallback shipped in September, this dropped from 81 to 21. The
remaining pages are mostly section indexes with empty content: `/journal/`,
`/journal/ailanthus/`, `/journal/woodpeckers/`, `/guidelines/`, `/app/` and their
`ru`/`hy` variants.

### P8 — 58 titles exceed 65 characters

Worst cases: `/hy/journal/lusavorich/` (106), `/hy/guidelines/biodiversity/woodpeckers/`
(104), `/ru/guidelines/legal/draft-valuation/` (86). The `— Kanach Yerevan` suffix
pushes already-long titles past the SERP limit. Armenian and Russian titles are hit
hardest because words are longer.

### P9 — GA4 is polluted and cannot be prioritised on

| Channel        | Sessions (365d) | Engagement |
| -------------- | --------------: | ---------: |
| Direct         |           2,164 |      22.1% |
| Organic Search |             548 |      56.6% |
| Organic Social |             282 |      43.6% |

Direct traffic is dominated by low-engagement sessions from Singapore (571), the US
(404) and China (276); desktop engagement is 22.5% versus 45.0% on mobile. This is
almost certainly bot and crawler traffic, which inflates Direct and drags down the
English engagement rate (23.3%).

### P10 — Yandex and AI assistants are real but untended channels

- Yandex referrals (`yandex.ru`, `yandex.kz`, `ya.ru`) total ~39 sessions/year of a
  548-session organic base — meaningful for the Russian audience.
- `chatgpt.com` referrals appear as an "AI Assistant" channel (21 sessions).

### P11 — Minor housekeeping

- 60 alias/redirect pages are generated with the title `Redirect`. They are
  correctly excluded from `sitemap.xml` and carry a canonical tag plus meta refresh,
  so risk is low. Zola 0.19 hardcodes this template and it cannot be overridden.
- Zola reports 7 orphan pages with no internal links pointing to them.

## 3. Action items

| ID  | Action                                                          | Impact   | Effort | Target files                                           |
| --- | --------------------------------------------------------------- | -------- | ------ | ------------------------------------------------------ |
| A1  | Rewrite titles and descriptions for the top 12 impression pages | High     | 1–2 d  | page front matter (§4)                                 |
| A2  | Add a separate SEO title field so `<title>` ≠ H1                | High     | 0.5 d  | `templates/home.html`, `templates/index.html`          |
| A3  | Answer the "Active Citizen platform" query on its own terms     | High     | 0.5 d  | `content/status/cases/active-citizen/`                 |
| A4  | Make EAC pages substantive; stop PDFs outranking HTML           | Med-High | 1 d    | `content/guidelines/legal/eac-*.md`, `static/_headers` |
| A5  | Resolve the two duplicate page pairs                            | Med      | 0.5 d  | journal + guidelines/legal page pairs                  |
| A6  | Add descriptions to the 21 section pages                        | Med      | 0.5 d  | `content/**/_index.md`                                 |
| A7  | Trim the 58 over-long titles                                    | Med      | 1 d    | journal + legal front matter                           |
| A8  | Filter bots in GA4 and save an Organic-only segment             | Med      | 0.5 d  | GA4 property settings                                  |
| A9  | Register with Yandex Webmaster and add IndexNow                 | Med      | 0.5 d  | ops / DNS / `static`                                   |
| A10 | Add TL;DR / FAQ blocks to legal pages                           | Med      | 2 d    | `content/guidelines/legal/*`                           |
| A11 | Link the 7 orphan pages from relevant sections                  | Low-Med  | 0.5 d  | section indexes                                        |
| A12 | Re-run `make seo` monthly and review targets                    | Ongoing  | —      | `docs/reports/`                                        |

### A2 — How to separate the SEO title from the H1

Add an optional `extra.seo_title` to front matter and use it in the two title blocks,
falling back to the current behaviour:

```html
{% block title %}{{ section.extra.seo_title | default(value=section.title) }} —
{{ config.title }}{% endblock %}
```

Then the H1 can stay `Kanach Yerevan` while the `<title>` becomes the value
proposition.

### A4 — PDF handling

Add a Cloudflare Pages `static/_headers` file:

```
/documents/*.pdf
  X-Robots-Tag: noindex
```

This keeps the standards downloadable and citable while redirecting ranking authority
to the HTML pages that explain them.

## 4. Proposed titles and descriptions (A1)

Replace the `title` in the relevant front matter and add/adjust `description`.
Armenian entries are marked **[HY — native review]**.

| Page                                     | Current title                                                 | Proposed title                                                            | Proposed description                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/`                                      | Kanach Yerevan                                                | Kanach Yerevan — protecting Yerevan's urban canopy                        | Independent monitoring, professional standards and legal tools to protect Yerevan's trees. Report damage, follow the cases, join the effort.                      |
| `/ru/`                                   | Kanach Yerevan                                                | Kanach Yerevan — защита зелёного фонда Еревана                            | Независимый мониторинг, профессиональные стандарты и юридические инструменты для защиты деревьев Еревана. Сообщить о проблеме, следить за делами, присоединиться. |
| `/hy/`                                   | Կանաչ Երևան                                                   | Կանաչ Երևան — Երևանի կանաչ ֆոնդի պաշտպանություն **[HY — native review]**  | Անկախ մշտադիտարկում, մասնագիտական չափորոշիչներ և իրավական գործիքներ Երևանի ծառերի պաշտպանության համար։                                                            |
| `/ru/guidelines/lawns/`                  | Газоны для Еревана                                            | Газон в Ереване: почему луговой газон лучше                               | Что такое луговой газон, почему он устойчивее обычного и как создать его во дворе многоквартирного дома Еревана.                                                  |
| `/hy/status/cases/active-citizen/`       | «Ակտիվ քաղաքացի» հարթակի միջոցով կանաչապատման մերժում (67)    | «Ակտիվ քաղաքացի» հարթակով բողոքարկելու ուղեցույց **[HY — native review]** | Ինչպես «Ակտիվ քաղաքացի» հարթակով բողոքել ծառահատման դեմ, ինչ պատասխան ստացանք և ինչ անել հաջորդ քայլով։                                                           |
| `/guidelines/legal/eac-pruning/`         | EAC Tree Pruning Standard                                     | European Tree Pruning Standard (EAC EAS 01:2021) explained                | What the European pruning standard requires, why it matters for Yerevan's trees, and how to use it when challenging a pruning permit.                             |
| `/status/alerts/komitas/`                | Proposal for Komitas Avenue renovation                        | Komitas Avenue: stop the mass felling of mature elms                      | Why replacing all mature trees on Komitas Avenue at once is a mistake, what we proposed, and how to support the alternative.                                      |
| `/guidelines/green-density/`             | Urban Greening: WHO Standards and the Reality of Yerevan (73) | Urban greening: WHO standards vs Yerevan reality                          | How much green space Yerevan residents actually have, and why the official statistics hide the shortfall.                                                         |
| `/ru/guidelines/leaves/`                 | Опавшие листья в городе: убирать или оставлять? (64)          | Опавшие листья: убирать или оставлять в Ереване                           | Аргументы за и против уборки листвы в городских условиях Еревана.                                                                                                 |
| `/ru/guidelines/biodiversity/great-tit/` | Синицы для Еревана                                            | Большая синица: как синичники помогают птицам Еревана                     | Почему большая синица важна для городских деревьев и как правильно повесить синичник во дворе Еревана.                                                            |
| `/guidelines/legal/gcap/`                | Green City Action Plan                                        | Green City Action Plan for Yerevan — what it promises                     | A 2017 strategy for Yerevan's environment: what it commits the city to, and what has actually changed since.                                                      |
| `/guidelines/legal/forest-code/`         | The Forest Code of the Republic of Armenia                    | Armenia's Forest Code: also applied to urban trees                        | Although it governs forests, its articles are often applied by analogy to Yerevan's street trees.                                                                 |

## 5. Measurement plan

| Horizon | Metric                                            | Baseline       | Target |
| ------- | ------------------------------------------------- | -------------- | -----: |
| 30 days | CTR on `/ru/guidelines/lawns/` (`gazon`, `газон`) | 3.4%           |     6% |
| 30 days | CTR on `/hy/status/cases/active-citizen/`         | 0.3%           |     2% |
| 60 days | CTR on the top 12 pages (blended)                 | ~2.8%          |     5% |
| 60 days | Total clicks per month                            | ~57 (Aug 2026) |     90 |
| 90 days | Brand-query CTR (`kanach` and variants)           | 0.3%           |     4% |
| 90 days | Non-brand clicks per month                        | ~11 (90 days)  |     40 |

Re-run `make seo` monthly; the regenerated report updates these baselines.

## 6. Data-quality caveats

- GA4 Direct traffic is inflated by bots (P9). Until filtering is configured, use
  **Search Console** for prioritisation and GA4 only for engagement on known-organic
  sessions.
- Search Console retains ~16 months; the property's earliest daily row is 2026-04,
  so trend analysis is limited.
- GA4 engagement for English (23.3%) is dragged down by the same bot traffic and
  should not be read as a content-quality signal yet.

## 7. What not to do

- Do not chase the `kanach` query with new pages — it is brand/entity noise. Fix the
  home page title and let the brand settle.
- Do not mass-auto-translate legal pages to fill language gaps; coverage is already
  complete except for 6 pages (`about/team`, `action/methods/*`, `app/*`).
- Do not add `noindex` to alias pages; they are already excluded from the sitemap and
  canonicalised, and Zola 0.19 does not allow overriding the redirect template.
