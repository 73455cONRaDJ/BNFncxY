# 代码生成时间: 2025-09-18 20:43:58
import numpy as np
import re
import sys

"""
Log Parser Tool

This tool is designed to parse log files and extract relevant information.
It is built using Python and NumPy.
"""

class LogParser:
    """Class responsible for parsing log files."""
    def __init__(self, logfile_path):
        """Initialize the LogParser with the provided log file path."""
        self.logfile_path = logfile_path
        self.pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d{3},\d{3} (INFO|ERROR|WARNING) (.*)"

    def parse_log(self):
        """Parse the log file and return a list of log entries."""
        try:
            with open(self.logfile_path, 'r') as file:
                logs = file.readlines()
            log_entries = []
            for line in logs:
                if re.match(self.pattern, line.strip()):
                    log_entries.append(line.strip())
            return log_entries
        except FileNotFoundError:
            print("Error: The log file was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

    def extract_info(self, log_entries):
        """Extract information from the log entries and return them in a structured way."""
        try:
            structured_logs = []
            for entry in log_entries:
                match = re.match(self.pattern, entry)
                if match:
                    date_time, severity, message = match.groups()
                    structured_logs.append({
                        'date_time': date_time,
                        'severity': severity,
                        'message': message
                    })
            return structured_logs
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

# Example usage
if __name__ == '__main__':
    parser = LogParser('path_to_log_file.log')
    log_entries = parser.parse_log()
    structured_logs = parser.extract_info(log_entries)
    for log in structured_logs:
        print(log)