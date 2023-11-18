import tempfile
from pathlib import Path
from typing import Generator

import pytest

from ..utils.funcs import read_toml, validate_and_create_dirs


@pytest.fixture
def valid_sample_toml_content() -> str:
    """
    Fixture: Providing a sample TOML content as a string.

    Returns:
        str: Sample TOML content.
    """
    return 'key = "value"'


@pytest.fixture
def invalid_sample_toml_content() -> str:
    """
    Fixture: Providing a sample TOML content as a string.

    Returns:
        str: Sample TOML content.
    """
    return "invalid data for toml files."


@pytest.fixture
def valid_temp_toml_file_path(valid_sample_toml_content: str) -> Generator:
    """
    Fixture: Creating a temporary TOML file with the sample content and yielding its
    Path.

    Args:
        valid_sample_toml_content (str): Sample TOML content.

    Yields:
        Generator[Path]: Temporary TOML file path.
    """
    file = tempfile.NamedTemporaryFile(delete=False, suffix=".toml")
    file.write(valid_sample_toml_content.encode())
    file.close()
    file_path = Path(file.name)
    yield file_path
    file_path.unlink()


@pytest.fixture
def invalid_temp_toml_file_path(invalid_sample_toml_content: str) -> Generator:
    """
    Fixture: Creating a temporary TOML file with the sample content and yielding its
    Path.

    Args:
        valid_sample_toml_content (str): Sample TOML content.

    Yields:
        Generator[Path]: Temporary TOML file path.
    """
    file = tempfile.NamedTemporaryFile(delete=False, suffix=".toml")
    file.write(invalid_sample_toml_content.encode())
    file.close()
    file_path = Path(file.name)
    yield file_path
    file_path.unlink()


@pytest.fixture
def sample_handlers(tmp_path: Path):
    """
    Fixture that returns a sample dictionary of handlers with associated filenames.
    """
    handlers = {
        "handler1": {"filename": tmp_path / "path1/log.txt"},
        "handler2": {"filename": tmp_path / "path2/log.txt"},
        "handler3": {},
        "handler4": {"filename": tmp_path / "path1/log.txt"},
    }
    return handlers


def test_read_valid_toml_file(valid_temp_toml_file_path: Path) -> None:
    """
    Test case for checking if the read_toml function reads a valid TOML file correctly.

    Args:
        valid_temp_toml_file_path (Path): Path to the temporary TOML file.
    """
    actual = read_toml(path=valid_temp_toml_file_path)
    expected = {"key": "value"}
    assert actual == expected, f"expected `{expected}` but got `{actual}`"


def test_read_invalid_toml_file(invalid_temp_toml_file_path: Path) -> None:
    """
    Test case for checking if the read_toml function correctly handles the case where
    the specified TOML file has a syntax error.
    """
    with pytest.raises(SystemExit):
        read_toml(path=invalid_temp_toml_file_path)


def test_read_toml_file_not_found() -> None:
    """
    Test case for checking if the read_toml function correctly handles the case where
    the specified TOML file is not found.
    """
    with pytest.raises(SystemExit):
        read_toml(Path("nonexistence_file.toml"))


def test_validate_and_create_dirs_with_path_manager(sample_handlers: dict) -> None:
    """Test the validate_and_create_dirs function with PathManager."""
    paths = validate_and_create_dirs(sample_handlers)
    for path in paths:
        assert path.parent.exists(), (
            "Expect that the parent of the paths to "
            "be created, but they are not created!"
        )
