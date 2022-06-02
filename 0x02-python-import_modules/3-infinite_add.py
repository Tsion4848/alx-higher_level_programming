#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum = 0;
    for x in argv:
        sum = sum + int(argv[x])
    print(sum)
