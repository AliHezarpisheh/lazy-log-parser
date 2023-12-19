import os
import logging

from .log_file_parser import LogParser
from .utils.messages import ViewMessages, ErrorMessages

logger = logging.getLogger("core")


class LogParserView:
    """A class representing the user interface for the LogParser application."""

    def clear_screen(self) -> None:
        """Clears the terminal screen."""
        os.system("cls" if os.name == "md" else "clear")    # pragma: no cover

    def show_divider(self) -> None:
        """Prints a divider line to separate sections in the console."""
        print(ViewMessages.DIVIDER)

    def get_path(self) -> str:
        """
        Prompts the user to enter the path of the log file and returns the input.

        Returns:
            str: The user-entered path of the log file.
        """
        file_path = input(ViewMessages.GET_PATH)
        self.show_divider()
        return file_path

    def get_log_level(self) -> str:
        """
        Prompts the user to enter the log level for filtering. Validates the
        input against the valid log levels and returns the validated log level.

        Returns:
            str: The validated log level entered by the user.

        Raises:
            ValueError: If the entered log level is not valid.
        """
        log_level = input(ViewMessages.GET_LOG_LEVEL)
        valid_levels = LogParser.valid_levels

        if log_level.upper() not in valid_levels:
            msg = ErrorMessages.INVALID_LOG_LEVEL.format(
                valid_levels=self.valid_levels, value=log_level
            )
            logger.debug(msg)
            raise ValueError(msg)

        self.clear_screen()

        return log_level

    def action(self) -> str:
        """
        Prompts the user to enter the next action (`next` or `quit`). Validates
        the input and returns the validated action.

        Returns:
            str: The validated user action (`next` or `quit`).

        Raises:
            ValueError: If the entered action is not valid.
        """
        command = input(ViewMessages.COMMAND)
        if command.lower() in ("next", "quit"):
            self.clear_screen()
            return command

        logger.info(ErrorMessages.INVALID_COMMAND_LOG.format(command=command))
        raise ValueError(ErrorMessages.INVALID_COMMAND.format(command=command))
