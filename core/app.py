import logging

from log_parser import LogParserView
from log_parser import LogParser

logger = logging.getLogger("core")

parser = LogParser()
view = LogParserView()


def main() -> None:
    """
    Main entry point for the Log Parser application.

    1. Initializes the logging configuration.
    2. Creates instances of LogParser and LogParserView classes.
    3. Prompts the user for log file path and log level for filtering.
    4. Parses the log file lazily and prints the first line.
    5. Enters a loop, allowing the user to request the next log line or quit the
        application.
    """
    view.clear_screen()

    file_path = view.get_path()
    log_level = view.get_log_level()

    parser.file_path = file_path
    parser.log_level = log_level
    lazy_file = parser.parse()

    first_line = next(lazy_file)
    print(first_line)

    while True:
        command = view.action()

        if command.lower() == "next":
            line = next(lazy_file)
            print(line)
        elif command.lower() == "quit":
            break
