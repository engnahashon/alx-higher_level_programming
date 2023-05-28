#!/usr/bin/python3
"""Python module for task 6. Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:"""
    with open(filename, 'r', encoding='utf-8') as f:
        my_obj = f.read()
        json.loads(my_obj)
        f.close
