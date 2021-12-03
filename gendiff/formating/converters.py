import json


def convert_stylish(value):
    if not isinstance(value, str):
        return json.JSONEncoder().encode(value)
    return value
