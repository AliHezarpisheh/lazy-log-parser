from pathlib import Path

from core import main
from config import setup_logging

LOGGING_CONFIG_PATH = Path("logging.toml")

if __name__ == "__main__":
    setup_logging(logging_config_path=LOGGING_CONFIG_PATH)
    main()
