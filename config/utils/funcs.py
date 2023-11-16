import sys
import tomllib
from pathlib import Path


def read_toml(path: Path) -> dict:
    """
    Read a TOML file and return its content as a dictionary.

    Args:
        path (Path): The path to the TOML file.

    Returns:
        dict: The parsed content of the TOML file.
    """
    try:
        with path.open(mode="rb") as file:
            file = tomllib.load(file)
        return file
    except FileNotFoundError:
        print(f"\n\033[91mThis path is unreachable: `{path}`!")
        sys.exit()
    except tomllib.TOMLDecodeError:
        print(f"\n\033[91mSyntax Error in: `{path}`!")
        sys.exit()


def validate_and_create_dirs(handlers: dict[str, dict]) -> list[Path]:
    """
    Validate the configuration and create directories specified in handlers.

    Args:
        handlers (dict): Dictionary containing logging handlers.

    Note:
        The function checks for the existence of directories specified
        in the 'filename' attribute of each handler in the configuration.
        If the directories do not exist, they are created.
    """
    paths = list()
    for handler in handlers.values():
        handler_path = handler.get("filename", None)
        if handler_path:
            path = Path(handler_path)
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                paths.append(path)
    return paths
