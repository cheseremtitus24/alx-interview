#!/usr/bin/python3
"""Checks if all boxes in a list can be unlocked

This file can also be imported as a module and contains
the following functions:
    * canUnlockAll- checks that all boxes can be unlocked

"""


def canUnlockAll(boxes):
    """checks that all boxes can be opened.

    Parameters
    ----------
    boxes: list
            is a list of lists
    Returns:
    --------
    bool:
        True or False

    """
    det = {}
    idx = 0

    for box in boxes:
        if len(box) == 0 or idx == 0:
            det[idx] = -1
        for key in box:
            if (key < len(boxes)) and (key != idx):
                det[key] = key
        if (len(det) == len(boxes)):
            return True
        idx += 1
    return False
