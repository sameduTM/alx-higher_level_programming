#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    x = len(list_of_integers)
    i = 0
    if len(list_of_integers) == 0:
        return None
    for i in range(x - 1):
        sorted_list = []
        j = 0
        for j in range(x - 1):
            if list_of_integers[j] < list_of_integers[j+1]:
                temp = list_of_integers[j]
                list_of_integers[j] = list_of_integers[j+1]
                list_of_integers[j+1] = temp
    sorted_list = list_of_integers
    k = 0
    for k in range(x):
        return sorted_list[k]
    return sorted_list
