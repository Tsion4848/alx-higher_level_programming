#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    print("{:s}".format(data, end=""))
    f.close()
