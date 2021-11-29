PYTHON = python3

.PHONY = help test generate clean

help: ## This help page.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

test: ## Run tests
	${PYTHON} -m pytest

generate: ## Append logs to a file with a regular interval
	${PYTHON} utils/generate_logs.py

clean: ## Delete pycache directories
	@find . -type d -name __pycache__ -exec rm -r {} \+
