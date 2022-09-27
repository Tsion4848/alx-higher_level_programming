#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_integers == []:
        return None

    size = len(list_integers)
    if size == 1:
        return list_integers[0]
    elif size == 2:
        return max(list_integers)

    mid = int(size / 2)
    peak = list_integers[mid]
    if peak > list_integers[mid - 1] and peak > list_integers[mid + 1]:
        return peak
    elif peak < list_integers[mid - 1]:
        return find_peak(list_integers[:mid])
    else:
        return find_peak(list_integers[mid + 1:])
