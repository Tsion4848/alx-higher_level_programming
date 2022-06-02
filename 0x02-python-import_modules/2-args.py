#!/usr/bin/python3
if len(argv) == 1:
    print("{:d} argument: {:s}".format(len(argv), argv))
elif len(argv) > 1:
    print("{:d} arguments: {:s}".format(len(argv), argv))
elif len(argv) == 0:
    print("{:d} arguments.".format(len(argv))
