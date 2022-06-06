#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for x in my_list:
        if x % 2 == 0:
            copy[x] = True;
        else:
            copy[x] = False;
    return copy
