#!/usr/bin/python3
for x in range(0, 100):
    d1 = x / 10
    d2 = x % 10
    if x == 89:
        print("{:d}".format(x))
    elif d1 < d2:
        print("{:02d}".format(x), end=", ")
