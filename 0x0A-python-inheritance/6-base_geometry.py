#!/usr/bin/python3
"""
Module 6-base_geometry
Contains empty class BaseGeometry, with public instance method area that raises an exception msg
"""


class BaseGeometry:
    """
    Methods:
        area(self)
    """
    def area(self):
        """raise msg saying area not implemented"""
        raise Exception("area() is not implemented")
