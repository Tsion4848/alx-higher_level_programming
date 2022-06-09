#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        res = 0
        change = 0
        dictnums = {'I': 1, 'v': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for x in reversed(roman_string):
            change = dictnums[x]
            if result < change * 5:
                res = res + change
            else:
                res = res - change
            return res
    else:
        return 0
