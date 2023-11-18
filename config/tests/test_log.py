import logging
from pathlib import Path
from typing import Any

import pytest

from ..log import setup_logging


@pytest.fixture
def sample_config_path(tmp_path: Path) -> Path:
    """
    Fixture creates a temporary sample TOML configuration file for testing purposes.

    Parameters:
        tmp_path (Path): The temporary path where the configuration file will be
        created.

    Returns:
        Path: The path to the created sample configuration file.

    Note:
    The function uses a TOML-formatted string as content to simulate a configuration
    file. The created file is automatically deleted after the test that uses it is
    completed.
    """
    content = """
    version = 1

    [formatters.testFormatter]
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    [handlers.testHandler]
    class = 'logging.FileHandler'
    level = 'DEBUG'
    formatter = 'testFormatter'
    filename = 'path/to/test_file.log'
    mode = 'a'

    [loggers.testLogger]
    level = 'DEBUG'
    handlers = ['testHandler']
    """
    config_path = tmp_path / "sample.toml"
    with config_path.open(mode="w") as config_file:
        config_file.write(content)
    yield config_path
    log_path = Path("path/to/test_file.log")
    # Delete the file and all the dirs.
    log_path.unlink()
    log_path.parent.rmdir()
    log_path.parent.parent.rmdir()


def test_setup_logging(sample_config_path: Path, caplog: Any) -> None:
    """
    Tests the setup of logging configurations using a sample TOML configuration file.

    Parameters:
        sample_config_path (Path): The path to the sample TOML configuration file.
        caplog (Any): A pytest fixture for capturing log messages during testing.

    Test Steps:
    1. Reads the sample configuration file.
    2. Sets up logging using the provided configuration.
    3. Checks if the log file path is created.
    4. Logs a test message using the configured logger.
    5. Verifies that the test log message appears in the captured logs.

    Note:
    This test function assumes the existence of a 'log' module with a 'setup_logging'
    function that takes a configuration file path and sets up the logging configuration
    accordingly.
    """
    setup_logging(sample_config_path)

    # Test the creation of paths to log files.
    log_file_path = Path("path/to/")
    assert log_file_path.exists(), f"{log_file_path} is not created!"

    # Check if the logger work as expected.
    logger = logging.getLogger("testLogger")
    logger.info("Test log message.")

    assert "Test log message." == caplog.records[0].msg
