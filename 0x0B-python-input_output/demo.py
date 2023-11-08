#!/usr/bin/python3
import sys
x = len(sys.argv)
my_list = []
for i in range(1, x):
    with open('demo.txt', mode='a', encoding='utf-8') as f:
        my_list.append(sys.argv[i])
        f.write(str(sys.argv[i]))
