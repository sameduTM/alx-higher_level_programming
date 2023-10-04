#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 == 0:
        print("{}".format(chr(char).lower()), end='')
    else:
        print("{}".format(chr(char).upper()), end='')
