#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass

    print()

    return count
/Users/honkrm/Documents/alx-higher_level_programming/0x05-python-exceptions
