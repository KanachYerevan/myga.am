---
description: Execute the agreed-upon plan directly and verify all formatting and index updates.
agent: build
---

Use OpenCode's built-in tools for file inspection and exploration: `read` (view files or list directory contents), `glob` (find files by name/pattern), and `grep` (search file contents). Prefer these over shell commands such as `ls`, `cat`, `find`, `head`, `tail`, `sed`, `awk`, and `echo`. Reserve the shell for operations that require it: `git` commands, formatters, and build tools.

Execute the implementation plan agreed upon in this session directly without sub-agents:

1. Apply all planned document, graphic, or configuration changes directly.
2. For any new or modified Markdown documents, ensure a YAML frontmatter `summary` is present.
3. Run `make format index` to format files and update `doc-index.md`.
4. Provide a concise summary of:
   - Modified/created files.
   - Any follow-up steps or notes.
