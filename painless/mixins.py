import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger("core")


class FileMixins:
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
            return path
        elif isinstance(path, str):
            path = Path(path)
            return path
        else:
            msg = f"path should be Path `object` or `str`, got `{type(path)}`"
            logger.debug(msg)
            raise ValueError(msg)

    @staticmethod
    def is_path_exists(path: Path) -> bool:
        """Check if a given path exists."""
        if not isinstance(path, Path):
            msg = f"path should be a Path object, but got `{type(path)}`"
            logger.debug(msg)
            raise ValueError(msg)

        return path.exists()
