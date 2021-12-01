import json

from gendiff.formating.common_json_stylish import generate_json_stylish


def convert_for_stylish(value):
    if not isinstance(value, str):
        return json.JSONEncoder().encode(value)
    return value


def generate_stylish(comparison):
    converter = convert_for_stylish
    return generate_json_stylish(comparison, converter)
