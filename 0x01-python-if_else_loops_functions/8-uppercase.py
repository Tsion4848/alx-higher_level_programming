#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            y = ord(x) - 32
        elif ord(x) >= 65 and ord(x) <= 90:
            y = ord(x)
        else:
            y = ord(x)
        print("{:s}".format(chr(y)), end="")
    print()
