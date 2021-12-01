import json

from gendiff.formating.common_json_stylish import generate_json_stylish


def generate_json(comparison):
    converter = json.JSONEncoder().encode
    return generate_json_stylish(comparison, converter)
