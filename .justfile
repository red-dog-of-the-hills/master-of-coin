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

verify: format-check lint-check type-check test

dev-server:
  APP_ENV=DEV python -m api
