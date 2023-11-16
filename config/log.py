from pathlib import Path
import logging.handlers
import logging.config
from typing import Dict

from .utils.funcs import read_toml, validate_and_create_dirs


def setup_logging() -> None:
    """Setup the logging configurations."""
    LOGGING_CONFIG_PATH = Path("logging.toml")
    logging_config = read_toml(path=LOGGING_CONFIG_PATH)
    # Check or Create the dirs of log files specified in the config.
    handlers: Dict[str, dict] = logging_config.get("handlers", None)
    validate_and_create_dirs(handlers=handlers)
    logging.config.dictConfig(logging_config)
