#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes (only the least significant 8 bits matter).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Mask to get only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count number of leading 1s
            mask = 0x80
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For the remaining bytes, they must start with '10'
            if (byte & 0xC0) != 0x80:
                return False

        num_bytes -= 1

    return num_bytes == 0
