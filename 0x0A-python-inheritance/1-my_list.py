#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """inherits from list that is passsed as an argument to MyList
    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order as requested"""
        print(list.sort())
