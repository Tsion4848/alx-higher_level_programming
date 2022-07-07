#!/usr/bin/python3
__import__("my_module").__doc__
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()
