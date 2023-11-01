from enum import StrEnum


class ErrorMessages(StrEnum):
    """Enumeration of error messages used in the LogParser application."""

    INVALID_LOG_LEVEL = "Valid log levels are: {valid_levels}, but got `{value}`"
    WRONG_PATH = "The given path is wrong. Please provide a valid file path."
    WRONG_PATH_LOG = "Valid path sent by the user: `{path}`"
    NO_PERMISSION = "You do not have the permission to read this file!"
    NO_PERMISSION_LOG = (
        "A file path that the user don't have permission to " "read it: `{path}`"
    )
    INVALID_COMMAND = "{command} is not a valid action, enter next or quit."
    INVALID_COMMAND_LOG = "user entered an invalid command: {command}"


class ViewMessages(StrEnum):
    """Enumeration of view messages used in the LogParser application."""

    DIVIDER = "------"
    GET_PATH = "Enter the path of your log file: "
    GET_LOG_LEVEL = "Enter the log level you want to filter by: "
    COMMAND = (
        "Enter `next` for seeing the next line or `quit` for quitting " "the app: "
    )
