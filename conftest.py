import pytest
from dynaconf import settings
import os

def pytest_addoption(parser):
    parser.addoption("--settings", action="store", default="default", help="指定环境")

def pytest_sessionstart(session):
    env = session.config.getoption("settings")
    settings.configure(INCLUDES_FOR_DYNACONF=['settings.toml', '*'], FORCE_ENV_FOR_DYNACONF=env)
    os.environ["env_setting"] = env