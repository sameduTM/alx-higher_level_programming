#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit != second_digit:
            print("{:02d}, ".format(first_digit * 10 + second_digit), end='')

