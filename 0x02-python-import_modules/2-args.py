#!/usr/bin/python3
import sys
x = sys.argv
if len(x) == 1:
    print("0 arguments.")
if len(x) == 2:
    print("1 argument:")
    print("1: {}".format(x[1]))
if len(x) > 2:
    print("{} arguments:".format(len(x) - 1))
    for i in range(len(x)):
        if i == 0:
            continue
        print("{}: {}".format(i, x[i]))
