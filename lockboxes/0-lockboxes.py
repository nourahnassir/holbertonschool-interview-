#!/usr/bin/python3
"""
Module for solving the lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
        boxes (list of lists): A list containing keys inside each box.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
