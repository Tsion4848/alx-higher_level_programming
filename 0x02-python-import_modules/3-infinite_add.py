#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    summ = 0
    for x in range(1, len(argv)):
        summ = summ + int(x)
    print("{:d}".format(summ))
