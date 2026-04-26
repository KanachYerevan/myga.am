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
	npx -y prettier --write $(MD_FILES)

deploy-cloudflare:
	npx wrangler pages deploy ./dist --project-name=myga --branch=master
