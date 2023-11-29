import os
import tempfile
from typing import Any
from pathlib import Path

import pytest

from ..log_file_parser import LogParser
from ..utils.messages import ErrorMessages


class TestLogParser:
    """Test class for the LogParser."""
    @pytest.fixture
    def log_parser(self) -> LogParser:
        """Fixture for creating a LogParser instance."""
        return LogParser()

    @pytest.fixture
    def sample_file_path(self, tmp_path: Path) -> Path:
        """Fixture for creating a sample file path."""
        file_path = tmp_path / 'test.log'
        file_path.touch()
        yield file_path
        file_path.unlink()
        file_path.parent.rmdir()

    def test_valid_file_path(
            self, log_parser: LogParser, sample_file_path: Path
    ) -> None:
        """
        Validates that the file path is correctly assigned to the LogParser instance.
        """
        log_parser.file_path = sample_file_path
        actual = log_parser.file_path
        expected = Path(sample_file_path)
        assert isinstance(actual, Path), (
            f"{actual} should be an Path object! got: " f"{type(actual)}"
        )
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_invalid_file_path(self, log_parser: LogParser) -> None:
        """Tests the LogParser's behavior when an invalid file path type is provided."""
        invalid_types = (12, 98.01, False, sum, None)
        for invalid_type in invalid_types:
            with pytest.raises(
                ValueError, match="path should be Path `object` or `str`"
            ):
                log_parser.file_path = invalid_type

    def test_valid_log_level(self, log_parser: LogParser) -> None:
        """Validates that the log level is correctly set in the LogParser instance."""
        log_parser.log_level = "debUg"
        actual = log_parser.log_level
        expected = "DEBUG"
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_invalid_log_level(self, log_parser: LogParser) -> None:
        """
        Tests the LogParser's behavior when an invalid log level value is provided.
        """
        with pytest.raises(ValueError, match="Valid log levels are:"):
            log_parser.log_level = "something_invalid"

    def test_invalid_log_level_type(self, log_parser: LogParser) -> None:
        """
        Tests the LogParser's behavior when an invalid log level type is provided.
        """
        with pytest.raises(AttributeError):
            log_parser.log_level = 12

    def test_parse(self, log_parser: LogParser, sample_file_path: Path) -> None:
        """
        Tests the laziness of the log parsing generator in the LogParser class.

        This test case ensures that the log parsing generator provided by the LogParser
        class exhibits lazy behavior. It verifies that the generator reads the log file
        lazily, yielding lines only when explicitly requested, without consuming the
        entire file at once.
        """
        content = "DEBUG: Test line 1\nINFO: Test line 2\nERROR: Test line 3"

        with sample_file_path.open(mode="w") as file:
            file.write(content)
            file.seek(0)

        log_parser.file_path = sample_file_path
        log_parser.log_level = "ERROR"
        generator = log_parser.parse()

        actual = next(generator)
        expected = "ERROR: Test line 3"
        assert actual == expected, f"expect {expected} but got {actual}"

        # Ensure that the generator is exhausted.
        with pytest.raises(StopIteration):
            next(log_parser.parse())

    def test_file_not_found_error(self, capsys: Any, log_parser: LogParser) -> None:
        """
        Tests the behavior of the LogParser when a FileNotFoundError occurs during
        parsing.
        """
        invalid_file_path = "/nonexistent/file.log"
        log_parser.file_path = invalid_file_path
        log_parser.log_level = "DEBUG"
        list(log_parser.parse())

        captured = capsys.readouterr()
        actual = captured.out
        expected = ErrorMessages.WRONG_PATH.value
        assert expected in actual, f"expect {expected} but got {actual}"


    def test_permission_error(self, capsys: Any, log_parser: LogParser) -> None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            no_permission_file_path = temp_file.name

        # Removing the read permission of the file.
        os.chmod(no_permission_file_path, 0o200)

        log_parser.file_path = no_permission_file_path
        log_parser.log_level = "DEBUG"
        list(log_parser.parse())

        captured = capsys.readouterr()
        actual = captured.out
        expected = ErrorMessages.NO_PERMISSION.value
        assert expected in actual, f"expect {expected} but got {actual}"

        # Tear down
        os.remove(no_permission_file_path)
