#!/usr/bin/python3
def common_elements(set_1, set_2):
    nums = [x if x == y for y in set_2 for x in set_1]
    return nums
