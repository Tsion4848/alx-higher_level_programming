#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w', encoding = "utf-8"):
        f.write(text)
    f.close()
