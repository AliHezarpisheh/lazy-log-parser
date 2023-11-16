from pathlib import Path

import pytest

from ..path_manager import PathManager


class TestPathManager:
    """Test suite for the PathManager class."""

    @pytest.fixture
    def sample_path(self, tmp_path: Path) -> Path:
        """Fixture that returns a temporary path for testing purposes."""
        return tmp_path / "path/to/random.txt"

    @pytest.fixture
    def path_manager(self, sample_path: Path) -> PathManager:
        """
        Fixture that returns an instance of PathManager with the provided sample path.
        """
        return PathManager(path=sample_path)

    def test_is_path_valid(self, path_manager: PathManager, sample_path: Path) -> Path:
        """
        Test whether the PathManager.path is a valid Path object and matches the
        expected path.
        """
        actual = path_manager.path
        expected = Path(sample_path)
        assert isinstance(actual, Path), (
            f"{actual} should be an Path object! got: " f"{type(actual)}"
        )
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_path_existence(self, path_manager: PathManager):
        """
        Test if the path exists by creating the parent directory and touching the file.
        """
        path_manager.path.parent.mkdir(parents=True, exist_ok=True)
        path_manager.path.touch()
        actual = path_manager.is_exist()
        expected = path_manager.path.exists()
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_path_none_existence(self, path_manager: PathManager, sample_path: Path):
        """Test if the path does not exist."""
        actual = path_manager.is_exist()
        expected = Path(sample_path).exists()
        assert actual == expected, f"expect {expected} but got {actual}"

    def test_make_parent_path(self, path_manager: PathManager) -> None:
        """Test the creation of the parent path."""
        path_manager.make()
        actual = path_manager.path.parent.exists()
        expected = True
        assert actual == expected, f"expect {expected} but got {actual}"
