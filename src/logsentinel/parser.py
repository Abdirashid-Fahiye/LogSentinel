import re

class LogParser:
    def __init__(self, filepath):
        self.filepath = filepath
        # Standard Apache/Nginx Regex Pattern
        self.log_pattern = re.compile(
            r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] '
            r'"(?P<method>[A-Z]+) (?P<url>.*?) HTTP/.*?" (?P<status>\d+) (?P<size>\d+)'
        )

    def parse_file(self):
        """Reads the log file and returns a list of extracted dictionaries."""
        results = []
        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    parsed_line = self.extract_regex(line)
                    if parsed_line:
                        results.append(parsed_line)
        except FileNotFoundError:
            print(f"Error: Log file not found at {self.filepath}")
        
        return results

    def extract_regex(self, line):
        """Applies regex to a single line. Returns None if the line is corrupted."""
        match = self.log_pattern.search(line)
        if match:
            return match.groupdict()
        return None