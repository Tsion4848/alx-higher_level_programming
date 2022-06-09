#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = a_dictionary.copy()
    for k in mult.keys():
        mult[k] = mult[k] * 2
    return mult
