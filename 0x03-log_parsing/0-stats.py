#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys

status_counts = {
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
line_counter = 0


def print_stats():
    """Prints the collected statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        line_counter += 1
        parts = line.strip().split()
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            pass

        if line_counter % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
