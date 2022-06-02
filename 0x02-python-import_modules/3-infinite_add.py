#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    summ = 0;
    for x in argv:
        summ = summ + int(argv[x] + 1)
    print(summ)
