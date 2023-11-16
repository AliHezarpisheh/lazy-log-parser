import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger("core")


class FileMixins:
    """
    A utility class providing methods for working with file paths.

    This class contains static methods to handle file paths, including converting
    paths to `Path` objects and checking if a given path exists.

    Example Usage:
    ```
    # Example usage of FileMixins class
    path = FileMixins.convert_to_path("/path/to/file.txt")
    if FileMixins.is_exists(path):
        print("File exists.")
    else:
        print("File does not exist.")
    ```
    """

    @staticmethod
    def convert_to_path(path: Union[Path, str]) -> Path:
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
            result = path
        elif isinstance(path, str):
            path = Path(path)
            result = path
        else:
            msg = f"path should be Path `object` or `str`, got `{type(path)}`"
            logger.debug(msg)
            raise ValueError(msg)

        return result

    @staticmethod
    def is_exist(path: Path) -> bool:
        """Check if a given path exists."""
        if not isinstance(path, Path):
            msg = f"path should be a Path object, but got `{type(path)}`"
            logger.debug(msg)
            raise ValueError(msg)

        return path.exists()
