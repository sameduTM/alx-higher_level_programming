#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()

    for item in my_list:
        if isinstance(item, int):
            unique_int.add(item)
    result = sum(unique_int)

    return result
