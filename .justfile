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
  python -m pytest --cov --cov-report=xml --cov-report=term-missing

verify: format-check lint-check type-check test-cov

dev-server:
  APP_ENV=DEV python -m api
