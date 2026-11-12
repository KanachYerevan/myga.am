MD_FILES := $(shell find AGENTS.md docs content -name "*.md")
# Use zola from PATH when available, otherwise the local copy in bin/.
ZOLA := $(shell command -v zola 2>/dev/null || echo ./bin/zola)

serve:
	$(ZOLA) serve

check:
	$(ZOLA) check

build:
	rm -rf dist
	mkdir -p dist
	$(ZOLA) build
	find dist -type f -print0 | xargs -0 ls -ldh

format:
	@npx -y prettier --write --list-different $(MD_FILES)

index:
	@echo "Updating doc-index.md ..."
	@grep 'summary:' -r . --include '*.md' --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules | sed -e 's/[[:space:]]*summary: / /g' | sed -e 's@^\./@@g' | sed -e 's@^@- @g' | sort > doc-index.md

seo:
	.venv/bin/python bin/seo/gsc_report.py
	.venv/bin/python bin/seo/ga4_report.py
	.venv/bin/python bin/seo/analyze.py

deploy-cloudflare:
	npx wrangler pages deploy ./dist --project-name=myga --branch=master
