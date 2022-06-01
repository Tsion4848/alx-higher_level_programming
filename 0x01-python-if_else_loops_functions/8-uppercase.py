#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            ord(x) = ord(x) - 32;
            print("{:s}".format(x), end="")
