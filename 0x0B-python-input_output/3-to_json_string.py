#!/usr/bin/python3
"""
Module 3-to_json_string
Contains function that returns JSON representation of obj (string): in python the alternative for json is a dictionary(if you dont import json)
"""


def to_json_string(my_obj):
    """Returns JSON representation of obj (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)