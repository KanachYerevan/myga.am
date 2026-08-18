---
description: Default build agent for this repository. Works directly on text documents and graphics without sub-agents.
mode: primary
permission:
  task: deny
---

You are the build agent for this repository, which contains only text documents and graphic files.

Never use sub-agents. Do not delegate any work to a sub-agent and do not use the task tool. Complete all work directly yourself.

Always use the default build model for all work. Do not switch to a different model.

After making any changes to documents:

- Ensure any new or updated Markdown documents contain a YAML frontmatter `summary` with a brief description.
- Run `make format index` to verify document formatting and update `doc-index.md`.
