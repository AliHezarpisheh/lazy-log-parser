# Log Parser

Welcome to Log Parser, a Python-based command-line tool designed for efficient parsing and analysis of log files. This application offers a streamlined user interface, allowing users to specify log file paths, filter log lines by specific log levels, and interactively view log entries.

## Features

- **Lazy Log Parsing:** Parses large log files lazily, ensuring memory efficiency by processing lines one at a time.
- **Flexible Log Filtering:** Filters log entries based on specified log levels (DEBUG, INFO, ERROR, WARNING, CRITICAL).
- **Interactive User Interface:** Provides an intuitive command-line interface for users to navigate log entries interactively.
- **Error Handling:** Handles invalid user inputs, wrong file paths, and permission issues gracefully, ensuring a smooth user experience.
- **Modular and Organized:** Utilizes modular architecture with clear separation of concerns, making the codebase easy to understand and maintain.
- **Logging:** Implements structured logging for debugging and error tracking, ensuring transparency in the application's behavior.

## Usage

1. **Run the Application:** Execute the main script to initiate the Log Parser application.
2. **Specify Log File:** Enter the path of the log file you want to analyze.
3. **Set Log Level:** Define the log level (DEBUG, INFO, ERROR, WARNING, CRITICAL) to filter log entries.
4. **Interactive Navigation:** Use the 'next' command to view the next log entry or 'quit' to exit the application.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AliHezarpisheh/lazy_log_parser.git
   cd lazy_log_parser
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python run.py
   ```

## Contributions

Contributions are welcome! Please follow these steps if you want to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and create a pull request.

---

Happy parsing!
