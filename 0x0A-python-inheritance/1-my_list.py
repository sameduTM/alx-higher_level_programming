#!/usr/bin/python3
"""This is the module doc"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        None

    Methods:
        print_sorted(): Print the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.

        This method sorts the list in ascending order and

        then prints the sorted list.
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
