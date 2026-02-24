format-check:
  black --check .
  ruff format --check

lint-check:
  ruff check

test:
  pytest
