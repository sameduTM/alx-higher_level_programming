#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            result += upper_char
        else:
            result += char
    print("{}".format(result))
