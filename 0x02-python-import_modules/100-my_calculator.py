#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
x = sys.argv
if __name__ == "__main__":
    if len(x) < 2:
        exit(1)
    a = int(x[1])
    op = x[2]
    b = int(x[3])
    if len(x) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == '+':
        res = add(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    if op == '-':
        res = sub(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    if op == '*':
        res = mul(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
    if op == '/':
        res = div(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
