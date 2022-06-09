#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for x in my_list:
        if my_list.count(x) == 1:
            sum = sum + x
        else:
            sum = sum + 0
    return sum
