#!/usr/bin/python3
import sys
import signal
import re

# Dictionary to count each status code
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0

# Regular expression to match the valid log line
log_pattern = re.compile(
    r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status, size = match.groups()
            try:
                total_size += int(size)
                if status in status_codes:
                    status_codes[status] += 1
            except ValueError:
                pass
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
