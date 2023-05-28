#!/usr/bin/python3
"""Python module task 5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        my_json = json.dumps(my_obj)
        f.write(my_json)
        f.close
