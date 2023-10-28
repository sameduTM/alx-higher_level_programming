#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [0] * len(my_list)
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        new_list[i] = my_list[i]
    new_list.insert(idx, element)
    if idx >= len(my_list):
        new_list.pop(idx - 1)
    elif idx < len(my_list):
        new_list.pop(idx + 1)
    return new_list
