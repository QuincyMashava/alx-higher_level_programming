#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains function that creates a Python obj from JSON file: in python the alternative for json is a ditcionary if you dont import it
"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file passed as argunment
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
