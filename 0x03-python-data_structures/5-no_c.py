#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if x != 'c' or x != 'C':
            copy[x] = my_string[x]
        return copy
