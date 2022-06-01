#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            y = ord(x) - 32;
            if chr(y) != str[length - 1]:
                print("{:s}".format(chr(y)), end="")
            else: 
                print("{:s}".format(chr(y)))
