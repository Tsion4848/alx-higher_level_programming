#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for x in my_list:
        if my_list.count(x) == 1:
            add= add + x
        else:
            add = add + 0
    return add
