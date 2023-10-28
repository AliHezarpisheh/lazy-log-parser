from pathlib import Path
from typing import Union


class DirLib:
    """A class providing basic operations related to directories.

    Usage:
        directory = DirLib("/path/to/directory")
        if directory.is_exist():
            print("Directory exists!")
        else:
            print("Directory does not exist. Creating it...")
            directory.make()
    """
    def __init__(self, path: Union[str, Path]) -> None:
        """Initialize DirLib object with a given path."""
        self._path = self._convert_to_path(path)

    @property
    def path(self) -> Path:
        """
        Get the current directory path.

        Returns:
            Path: The directory path.
        """
        return self._path

    def _convert_to_path(self, path: Union[Path, str]) -> Path:
        """
        Convert the input path to a Path object.

        Args:
            path (Union[Path, str]): The input path.

        Returns:
            Path: The converted Path object.

        Raises:
            ValueError: If the input path is not a valid Path object or string.
        """
        if isinstance(path, Path):
            return path
        elif isinstance(path, str):
            path = Path(path)
            return path
        else:
            raise ValueError(
                f"path should be Path `object` or `str`, got `{type(path)}`"
            )

    def is_exist(self) -> bool:
        """Check if a given path exists."""
        return self.path.exists()

    def make(self) -> None:
        """Create a new path (including nested paths)."""
        self.path.parent.mkdir(parents=True,)
