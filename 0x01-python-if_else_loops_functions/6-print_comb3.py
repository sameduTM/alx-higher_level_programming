#!/usr/bin/python3
for r in range(0, 89):
    if r % 10 > r // 10:
        print("{:02}".format(r), ", ", sep='', end='')
print("89")
