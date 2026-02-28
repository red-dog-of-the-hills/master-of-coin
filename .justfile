format-check:
  black --check .
  ruff format --check

lint-check:
  ruff check

test:
  pytest

test-cov:
  python -m pytest --cov
