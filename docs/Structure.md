# Website Content Structure

This document outlines the organization of the Kanach Yerevan website. The site is organized based on user intent rather than file type, ensuring that visitors find information exactly where they expect it.

## The Five Main Sections

The content is divided into five primary areas.

The Guidelines section functions as the documentation site for the city. It contains authoritative standards rather than blog posts. General standards like pruning, mulching, and planting live here. It also includes a Biodiversity subsection for protocols on feeding and nesting, as well as specific bird species profiles. Finally, the Legal subsection contains the formal codes and regulations.

The Monitor section acts as our data hub and proof of work. It contains Street Passports, which are periodic health assessments of specific streets or parks. It also houses the Cases section, where we track specific incidents like illegal cuttings and our response to them. Urgent, temporary alerts regarding immediate threats to the urban canopy are also posted here.

The Action section is the entry point for users who want to participate. It contains instructions on how to use our app or hotline to report issues, information on volunteering or donating, and a calendar of upcoming events. Note that the instructions on "how to report" live here, while the actual tracked cases live in the Monitor section.

The Journal section replaces the traditional blog. This is the place for field notes, success stories, press releases, and general updates about the movement.

The About section contains institutional information, including our mission statement, team members, and the Green Directory, which lists trusted nurseries and suppliers.

## Managing Images and Documents

We use two primary methods for managing assets:

1. **Page Bundles (Recommended):** For images or documents that belong to a specific page, we use Page Bundles. Instead of a single `page.md` file, we create a directory named `page/` with `index.md` (and any translation files like `index.ru.md`) inside it. All assets for that page are placed directly in the same folder. This allows for relative links and makes the content more portable.

2. **Global Assets (`static/`):** Shared assets (logos, common icons, or files used across multiple pages) go directly into the `static/images/` or `static/documents/` folder. Since these files are shared, you must use unique, descriptive filenames (e.g., `logo-owl.png`) to prevent conflicts.

## Page Settings and Metadata

Every page requires specific settings at the very top of the file to help the website display it correctly.

For Guidelines pages, you must define a status (Recommended, Prohibited, or Caution) and a short verdict. This allows the site to display a clear visual label, like a green "Recommended" banner, at the top of the article.

For Case files in the Monitor section, you need to track the progress of the incident. You must specify the current status (Open, Won, Lost, or Stalled), the location (district name), and the date the case was opened. This helps us generate statistics and filter cases on the main dashboard.

## Maintenance and Frequency

Different parts of the website need different levels of attention.

The Journal is the heartbeat of the site. It should be updated frequently to show visitors that we are active. Aim for at least one update per month.

The Monitor section relies on trust. If you open a Case or start a Street Passport, you must keep it updated. An "Open" case that has not been touched in a year looks worse than no case at all.

The Guidelines are our long-term reference library. These only need to be changed if the laws change or if we decide to recommend a new technique.

## Example Directory Structure

Below is an example of how the files should be organized on disk. Note the use of Page Bundles for complex pages like `pruning` and `lawns`.

```
content/
├── guidelines/
│   ├── _index.md
│   ├── pruning/
│   │   ├── index.md
│   │   ├── index.ru.md
│   │   ├── branch-cut.jpg
│   │   └── crown-thinning.png
│   ├── mulching.md
│   ├── lawns/
│   │   ├── index.md
│   │   └── biodiversity.jpg
│   ├── planting.md
│   │
│   ├── biodiversity/
│   │   ├── _index.md
│   │   ├── feeding-standards.md
│   │   ├── nesting-standards.md
│   │   ├── great-tit.md
│   │   └── woodpecker.md
│   │
│   └── legal/
│       ├── _index.md
│       ├── administrative.md
│       └── construction.md
│
├── status/
│   ├── _index.md
│   ├── map.md
│   │
│   ├── passports/
│   │   ├── _index.md
│   │   ├── mashtots-ave.md
│   │   └── abovyan-st.md
│   │
│   ├── cases/
│   │   ├── _index.md
│   │   ├── case-2024-01-opera.md
│   │   └── case-2024-05-cascade.md
│   │
│   └── alerts/
│       ├── _index.md
│       └── 60-percent-cut.md
│
├── action/
│   ├── _index.md
│   ├── report-issue.md
│   ├── volunteer.md
│   └── events.md
│
├── journal/
│   ├── _index.md
│   ├── 2024-10-success.md
│   └── 2024-11-update.md
│
└── about/
    ├── _index.md
    ├── mission.md
    ├── team.md
    └── directory.md
```

## Shared Assets (static/)

Global assets used across multiple pages.

```
static/
├── images/
│   ├── logo-owl.png
│   └── favicon.ico
│
└── documents/
    ├── general-charter.pdf
    └── legal-draft-text.pdf
```
