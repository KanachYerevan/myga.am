---
name: Content Refactor
description: Merge, split, rename or delete pages under content/, keeping en/ru/hy in step, front matter honest, redirects intact and doc-index regenerated.
summary: "Procedure for merging, splitting, renaming or deleting a content page while keeping translations, redirects, weights and doc-index consistent."
---

# Content Refactor

Site copy lives in three languages and Zola derives every URL from the folder name. Restructuring a page touches more than the page.

## Before editing

1. Read every language variant (`index.md`, `.ru.md`, `.hy.md`) and the section `_index` in each language. Front matter must stay in step across all three.
2. Grep the repository for the old path and for inbound links to it. Relative links in other pages break silently, and a `../` link inside the page being merged becomes a self-link.
3. Decide the URL story before deleting anything. A removed page needs 301s in `static/_redirects`: with and without a trailing slash, for `/`, `/ru/` and `/hy/`. Point any pre-existing redirects at the final destination so nobody gets a chain.
4. Check `weight` against sibling pages before touching it. Sections sort by weight, not alphabetically, and the municipal and national groups are separated by weight bands.

## Front matter that carries weight

- `description` renders in section rows and as the meta/OG description. Write it for a reader, not as an inventory of the file.
- `summary` feeds `doc-index.md` through `make index`, and is the fallback description for cards.
- `extra.title` overrides `title` in section rows.
- Leave `date` alone unless the document's own date changed.

## After editing

1. Run `make format index`. Never hand-edit `doc-index.md`.
2. Run `./bin/zola build`. It must report no broken internal links.
3. Look at the built HTML for the one thing the edit was about: a row title, heading order, button placement, list nesting. Stop there.
