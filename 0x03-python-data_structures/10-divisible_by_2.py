#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = ""
    for x in my_list:
        if x % 2 == 0:
            copy = copy + True
        else:
            copy = copy + False
    return copy
