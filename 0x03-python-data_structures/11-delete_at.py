#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    x = len(my_list)
    if idx < 0 or idx > x:
        return my_list
    for i in range(x):
        if i == idx:
            continue
        new_list.append(my_list[i])
    return new_list
