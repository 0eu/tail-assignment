PYTHON = python3

.PHONY = help test generate

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run log seeder type make generate"
	@echo "------------------------------------"

test:
	${PYTHON} -m unittest tests/test_tail.py

generate:
	${PYTHON} utils/generate_logs.py

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
