import logging
from pathlib import Path
from typing import Generator

from painless.mixins import FileMixins
from .utils.type_hints import LogLevel
from .utils.messages import ErrorMessages

logger = logging.getLogger("core")


class LogParser(FileMixins):
    """
    A class for parsing log files and extracting lines based on specified log
    levels.
    """

    valid_levels = ("DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL")

    def __init__(
        self, file_path: Path, log_level: str = "ERROR"
    ) -> None:
        """
        Initializes LogParser instance with the provided file path and loglevel.

        Args:
            file_path (str): The path to the log file. Defaults to "example.log"
            log_level (str, optional): The desired log level for filtering log
                lines. Defaults to "ERROR".
        """
        self.file_path = file_path
        self.log_level = log_level

    @property
    def file_path(self) -> Path:
        """
        The property for the file_path.

        Returns:
            Path: The file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, value: str) -> None:
        """
        Setter for the file_path attribute. Convert the provided file_path
        to a path object.

        Args:
            value (str): The new file_path.
        """
        self._file_path = self.convert_to_path(path=value)

    @property
    def log_level(self) -> LogLevel:
        """
        The property for the log level.

        Returns:
            LogLevel: The log level as a string.
        """
        return self._log_level

    @log_level.setter
    def log_level(self, value: str) -> None:
        """
        Setter for the log level attribute. Validates that the provided log level
        is valid.

        Args:
            value (str): The new log level.

        Raises:
            ValueError: If the provided log level is not in the valid_levels
                attribute.
        """
        if value.upper() not in self.valid_levels:
            msg = ErrorMessages.INVALID_LOG_LEVEL.format(self.valid_levels, value)
            logger.debug(msg)
            raise ValueError(msg)

        self._log_level = value.upper()

    def parse(self) -> Generator:
        """
        Lazily parses the log file and yields lines matching the specified log level.

        Yields:
            str: Log lines matching the specified log level.
        """
        try:
            # Check that is the log file is opened before and saved or not. This
            # is for preventing the file to be reopened every time the next() is
            # called on the generator.
            if not hasattr(self, "_log_file"):
                self._log_file = self.file_path.open(mode="r")

            for line in self._log_file:
                if self.log_level in line:
                    yield line
        except FileNotFoundError:
            print(ErrorMessages.WRONG_PATH)
            logger.info(ErrorMessages.WRONG_PATH_LOG.format(self.file_path))
        except PermissionError:
            print(ErrorMessages.NO_PERMISSION)
            logger.info(ErrorMessages.NO_PERMISSION_LOG.format(self.file_path))
