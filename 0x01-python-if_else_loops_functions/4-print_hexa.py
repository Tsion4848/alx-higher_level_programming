#!/usr/bin/python3
for x in range(0, 98):
    print("{:d} = 0x{:s}".format(x, x.encode('hex')))
