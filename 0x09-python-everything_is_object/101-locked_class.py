#!/usr/bin/python3
"""
Defines class with no class or object attribute
Control dynamically created instance attributes
Found this site to be useful, please visit https://www.python-course.eu/python3_slots.php
"""


class LockedClass():
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    >>> a = LockedClass()
    >>> a.first_name = 'Quincy'
    >>> a.first_name
    'Quincy'
    >>> a.last_name = 'Mashava'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
