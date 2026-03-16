test:
	pytest

test-watch:
	ptw -- -v

# Run a specific test file: make test-one filter=01_chai
test-one:
	pytest -v -k "$(filter)"

install:
	pip install -r requirements.txt
