#!/usr/bin/python3
"""This is the My list module"""


class MyList(list):
    """This is the only class of module"""
    def print_sorted(self):
        if issubclass(isinstance()):
            pass
        if all(isinstance(element, int) for element in self):
            try:
                sorted_list = sorted(self)
                # print(sorted_list)
                return sorted_list
            except Exception as e:
                print(e)
        return self