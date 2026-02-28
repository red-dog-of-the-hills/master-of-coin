format-check:
  ruff format --check

format:
  ruff format

lint-check:
  ruff check

type-check:
  pyright

test:
  pytest

test-cov:
  python -m pytest --cov --cov-report=xml
