#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            y = ord(x) - 32;
            if (chr(y) != x[-1]): 
                print("{:s}".format(chr(y)), end="")
print()
