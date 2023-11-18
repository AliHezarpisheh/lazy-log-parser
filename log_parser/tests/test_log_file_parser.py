from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from ..log_file_parser import LogParser


class TestLogParser:
    @pytest.fixture
    def log_parser(self) -> LogParser:
        return LogParser()

    @pytest.fixture
    def sample_file_path(self, tmp_path: Path) -> Path:
        file_path = tmp_path / 'test.log'
        file_path.touch()
        return file_path

    @pytest.fixture
    def valid_levels(self) -> tuple[str, ...]:
        levels = ("DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL")
        return levels

    def test_valid_file_path(
            self, log_parser: LogParser, sample_file_path: Path
    ) -> None:
        log_parser.file_path = sample_file_path
        actual = log_parser.file_path
        expected = Path(sample_file_path)
        assert isinstance(actual, Path), (
            f"{actual} should be an Path object! got: " f"{type(actual)}"
        )
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_invalid_file_path(self, log_parser: LogParser) -> None:
        invalid_types = (12, 98.01, False, sum, None)
        for invalid_type in invalid_types:
            with pytest.raises(
                ValueError, match="path should be Path `object` or `str`"
            ):
                log_parser.file_path = invalid_type

    def test_valid_log_level(self, log_parser: LogParser) -> None:
        log_parser.log_level = "debUg"
        actual = log_parser.log_level
        expected = "DEBUG"
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_invalid_log_level(self, log_parser: LogParser) -> None:
        with pytest.raises(ValueError, match="Valid log levels are:"):
            log_parser.log_level = "something_invalid"

    def test_invalid_log_level_type(self, log_parser: LogParser) -> None:
        with pytest.raises(AttributeError):
            log_parser.log_level = 12

    def test_parse(self, log_parser: LogParser, sample_file_path: Path) -> None:
        file_path = Path("mioo.log")
        content = "DEBUG: Test line 1\nINFO: Test line 2\nERROR: Test line 3"

        with file_path.open(mode="a") as file:
            file.write(content)

        log_parser.file_path = file_path
        log_parser.log_level = "ERROR"
        result = log_parser.parse()
        result = next(result)
        breakpoint()