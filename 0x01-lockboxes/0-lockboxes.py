#!/usr/bin/python3
"""Check if all boxes can be unlocked using keys from other boxes."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list where each element is a list
        of keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    opened = set([0])  # Start with box 0 as opened
    stack = [0]        # Stack for DFS

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if (
                isinstance(key, int) and
                0 <= key < len(boxes) and
                key not in opened
            ):
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
