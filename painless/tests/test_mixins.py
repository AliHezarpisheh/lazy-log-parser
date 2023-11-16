from pathlib import Path

import pytest

from ..mixins import FileMixins


class TestFileMixins:
    """Test suite for the FileMixins class."""

    @pytest.fixture
    def file_handler(self) -> FileMixins:
        """Fixture that returns an instance of FileMixins."""
        return FileMixins()

    @pytest.fixture
    def sample_str_path(self, tmp_path: Path) -> str:
        """
        Fixture that returns a string representation of a temporary path for testing.
        """
        return str(tmp_path / "path/to/random.txt")

    @pytest.fixture
    def sample_path(self, tmp_path: Path) -> Path:
        """Fixture that returns a Path object for testing."""
        return tmp_path / "path/to/random.txt"

    @pytest.fixture
    def sample_existing_path(self, tmp_path: Path) -> Path:
        """Fixture that returns an existing Path object for testing."""
        path = tmp_path / "path/to/existed.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        return path

    def test_str_to_path(self, file_handler: FileMixins, sample_str_path: str) -> None:
        """Test converting a string path to a Path object."""
        actual = file_handler.convert_to_path(sample_str_path)
        expected = Path(sample_str_path)

        assert isinstance(actual, Path), (
            f"{actual} should be an Path object! got: " f"{type(actual)}"
        )
        assert actual == expected

    def test_path_to_path(self, file_handler: FileMixins, sample_path: Path) -> None:
        """Test converting a Path object to itself."""
        actual = file_handler.convert_to_path(sample_path)
        expected = Path(sample_path)

        assert isinstance(actual, Path), (
            f"{actual} should be an Path object! got: " f"{type(actual)}"
        )
        assert actual == expected

    def test_invalid_object_to_path(self, file_handler: FileMixins) -> None:
        """Test handling invalid types when converting to a Path object."""
        invalid_types = (12, 10.02, True, open)
        for invalid_type in invalid_types:
            with pytest.raises(
                ValueError, match="path should be Path `object` or `str`"
            ):
                file_handler.convert_to_path(invalid_type)

    def test_path_existence(
        self, file_handler: FileMixins, sample_existing_path: Path
    ) -> None:
        """Test checking the existence of an existing path."""
        actual = file_handler.is_exist(sample_existing_path)
        expected = True
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_path_none_existence(
        self, file_handler: FileMixins, sample_path: Path
    ) -> None:
        """Test checking the non-existence of a path."""
        actual = file_handler.is_exist(sample_path)
        expected = False
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_invalid_object_in_is_exists(self, file_handler: FileMixins) -> None:
        """Test handling invalid types when checking existence."""
        invalid_types = (12, 10.02, True, open)
        for invalid_type in invalid_types:
            with pytest.raises(ValueError, match="path should be a Path object"):
                file_handler.is_exist(invalid_type)
