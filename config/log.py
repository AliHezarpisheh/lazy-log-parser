import tomllib
from pathlib import Path
import logging.handlers
import logging.config
from typing import Dict

from painless import DirLib


CONFIG_PATH = Path("logging.toml")

with CONFIG_PATH.open(mode="rb") as config_file:
    config = tomllib.load(config_file)

# Check or Create the dirs of log files specified in the config.
handlers: Dict[str, dict] = config.get("handlers", None)
for handler in handlers.values():
    handler_path = handler.get("filename", None)
    if handler_path:
        directory = DirLib(handler_path)
        if not directory.is_exist():
            directory.make()


def setup_logging() -> None:
    """Setup the logging configurations."""
    logging.config.dictConfig(config)
