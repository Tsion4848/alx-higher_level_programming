#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        y = add(a, b)
        for x in range(4, 6):
            y = add(y, x)
            return(y)
    return(sub(a, b))
