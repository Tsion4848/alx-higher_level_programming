#!/usr/bin/python3
"""
add_integer function

This function adds two integers and returns an integer
"""


def add_integer(a, b = 98):
    """
    check if the parameters are float and if so, casted it to integer.
    if parameters are not integer or float, raise an exception message."""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if typr(b) == float:
        b = int(b)
    return a + b
