---
name: markdown
description: rules for formatting markdown documents and documentation. Use this whenever working with any files in the docs/ folder or any .md files.
---

## Markdown Formatting Rules

When creating or modifying markdown documents, you MUST adhere strictly to the following rules:

1. YAML frontmatter: always use YAML frontmatter delimited by `---` (not TOML `+++`). Include `title`, `description`, and a `summary` field (used for generating `doc-index.md`).
2. Minimal bold: never use bold in text unless absolutely necessary.
3. No numbered headers: do not use numbered headers (e.g., use `## Header` instead of `## 1. Header`).
4. Lowercase after colon in lists: in list items, the first letter immediately after a colon must be lowercase (e.g., "- key: value"). Capitalization in the rest of the sentence remains unchanged.
   - Bad: "- Foo: Bar"
   - Bad: "- Foo: bar"
   - Good: "- Foo: bar"
5. List spacing: always leave a blank line above and below a list, except for nested lists.
6. Post-processing: run `make format index` after any changes to markdown files.
