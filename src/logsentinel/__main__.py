import sys
from pathlib import Path
from src.logsentinel.reporter import Reporter

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.logsentinel <path_to_log_file>")
        sys.exit(1)
        
    log_path = sys.argv[1]
    reporter = Reporter(log_path)
    reporter.print_terminal_summary()

if __name__ == "__main__":
    main()