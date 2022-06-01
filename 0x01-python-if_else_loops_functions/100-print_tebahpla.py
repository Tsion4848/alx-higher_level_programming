#!/usr/bin/python3
for x in "zyxwvutsrqponmlkjhgfedcba":
    if ord(x) >= 97 and ord(x) <= 122 || ord(x) >= 65 && ord(x) <= 90:
        y = ord(x)
        print("{:s}".format(chr(y)), end="")
        y = y + 1
        y = ord(x) - 32
    else:
        y = ord(x)
