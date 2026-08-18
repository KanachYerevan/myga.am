MD_FILES := $(shell find AGENTS.md docs content -name "*.md")

serve:
	zola serve

check:
	zola check

build:
	rm -rf dist
	mkdir -p dist
	zola build
	find dist -type f -print0 | xargs -0 ls -ldh

format:
	@npx -y prettier --write --list-different $(MD_FILES)

index:
	@echo "Updating doc-index.md ..."
	@grep 'summary:' -r . --include '*.md' | sed -e 's/summary: / /g' | sed -e 's@^\./@@g' | sed -e 's@^@- @g' | sort > doc-index.md

deploy-cloudflare:
	npx wrangler pages deploy ./dist --project-name=myga --branch=master
