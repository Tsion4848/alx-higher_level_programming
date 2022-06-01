#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if int (str(i) + str(j)) == 89:
            print("{:d}{:d}".format(i, j))
        else if int(str(i) + str(j)) != int(str(j) + str(i)):
            print("{:d}{:d}".format(i, j), end=", ")
