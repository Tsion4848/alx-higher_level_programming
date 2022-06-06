#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for x in my_string:
        if my_string[x] != 'c' and my_string[x] != 'C':
            copy = copy + my_string[x]
        return copy
