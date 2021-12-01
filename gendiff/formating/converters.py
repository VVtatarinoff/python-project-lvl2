import json


def convert_for_stylish(value):
    if not isinstance(value, str):
        return json.JSONEncoder().encode(value)
    return value