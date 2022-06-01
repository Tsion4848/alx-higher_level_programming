#!/usr/bin/python3
for x in "abcdefghijklmnopqrstuvwxyz":
    if ord(x) >= 97 and ord(x) <= 122:
        y = ord(x)
        y = y + 1
        y = ord(x) - 32 
    elif ord(x) >= 65 and ord(x) <= 90:
        y = ord(x)
        y = y + 1
        y = ord(x) + 32
    else:
        y = ord(x)
    print("{:s}".format(chr(y)), end=""i)
