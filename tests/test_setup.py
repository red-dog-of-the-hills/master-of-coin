from api.config import Environment, get_config


def test_env() -> None:
    config = get_config()
    assert config.APP_ENV == Environment.TEST
