import logging

from pathlib import Path
from typing import Union

from .mixins import FileMixins

logger = logging.getLogger("core")


class DirLib(FileMixins):
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
        self._path = self.convert_to_path(path)

    @property
    def path(self) -> Path:
        """
        Get the current directory path.

        Returns:
            Path: The directory path.
        """
        return self._path

    def is_exists(self) -> bool:
        """Check if a given path exists using the is_path_exists method."""
        return super().is_path_exists(self.path)

    def make(self) -> None:
        """Create a new path (including nested paths)."""
        self.path.parent.mkdir(parents=True,)
