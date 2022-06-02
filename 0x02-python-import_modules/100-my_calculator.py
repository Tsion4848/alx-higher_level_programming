#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        y = argv[2]
        oper = {'+': add, '-': sub, '*': mul, '/': div}
        for x in oper:
            if y == x:
                print("{} {} {} = {}".format(a, y, b, oper[x](a, b)))
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
