#!/usr/bin/python3
import sys
x = sys.argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(x)):
        y = x[i]
        sum += int(y)
    print("{}".format(sum))
