import json
from json.decoder import JSONDecodeError


def convert_stylish(value):
    if not isinstance(value, str):
        return json.JSONEncoder().encode(value)
    return value


def convert_json(value):
    json_string = str(JSONDecodeError().encode(value))
    return json_string
