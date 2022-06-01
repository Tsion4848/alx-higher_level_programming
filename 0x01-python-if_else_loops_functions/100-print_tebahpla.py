#!/usr/bin/python3
for x in range(122, 96, -1):
    print("{:c}".format((x - 32) if x % 2 else x), end="")
