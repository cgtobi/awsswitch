"""AWS profile switcher"""
import configparser
import os
from pathlib import Path

from InquirerPy import prompt

__version__ = "0.0.1"


DEFAULT_PROFILE = "default"
HOME_DIRECTORY = "~"
AWS_PATH = ".aws"
AWS_CONFIG = "config"
AWS_CONFIG_FILE = "AWS_CONFIG_FILE"


def get_path() -> Path:
    """Get aws config path."""
    if aws_path_env := os.getenv(AWS_CONFIG_FILE):
        return Path(aws_path_env)

    return Path.home() / AWS_PATH


def profile_reader() -> list:
    """Read AWS profile."""
    config = configparser.ConfigParser()
    config.read(get_path() / AWS_CONFIG)
    return config.sections()


def app() -> None:
    """AWS profile switcher."""
    print("AWS profile switcher")
    questions = [
        {
            "type": "list",
            "message": "Choose a profile:",
            "choices": profile_reader(),
            "default": DEFAULT_PROFILE,
        },
    ]
    result = prompt(questions)
    print(result)


if __name__ == "__main__":
    app()
