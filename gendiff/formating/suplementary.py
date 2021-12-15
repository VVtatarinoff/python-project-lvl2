import json


def convert_non_string(value):
    if not isinstance(value, str):
        return json.JSONEncoder().encode(value)
    return value
