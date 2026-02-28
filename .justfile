format-check:
  black --check .
  ruff format --check

format:
  black .
  ruff format

lint-check:
  ruff check
  pyright

test:
  pytest

test-cov:
  python -m pytest --cov --cov-report=xml
