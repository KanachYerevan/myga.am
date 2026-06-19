# ADR 0002: Adopt Page Bundles for Asset Co-location

- Status: Accepted
- Date: 2026-06-19

## Context

Originally, the project followed a flat asset structure where all images were stored in `static/images/` and all documents in `static/documents/`. This was documented in `AGENTS.md` and `docs/Structure.md`.

As the site grows, this flat structure presents several challenges:

1. **Naming Collisions:** With many pages, finding unique descriptive names for images (e.g., `diagram.png`) becomes difficult.
2. **Maintenance Burden:** When moving or renaming a page, the associated images in `static/` must be manually tracked and updated.
3. **Cognitive Load:** Developers and editors have to jump between `content/` and `static/` folders to manage a single piece of content.
4. **Localization complexity:** Referencing the same image from multiple language versions (`.md`, `.ru.md`, `.hy.md`) is more verbose when using absolute paths to `static`.

## Decision

We will adopt Zola's **Page Bundles** (asset co-location) as the primary method for managing page-specific assets.

1. Instead of `page.md`, use a directory `page/` with `index.md` (and translations like `index.ru.md`).
2. Assets used exclusively by that page should be placed inside the same directory.
3. Reference these assets using relative paths in Markdown.
4. Shared assets (logos, common icons) will remain in `static/`.

## Consequences

### Positive:

- **Improved Portability:** Moving a folder moves both the text and its images.
- **Simplified Naming:** Images can have simple names (e.g., `map.jpg`) because they are scoped to the page directory.
- **Better Developer Experience:** Content and its dependencies are co-located.
- **Idiomatic Zola:** This aligns with Zola's recommended way of handling non-shared assets.

### Negative:

- **Mixed Content/Assets:** The `content/` directory will now contain binary files (images), not just text.
- **Migration Effort:** Existing pages with many images may need to be restructured over time to maintain consistency.
