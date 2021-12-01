from gendiff.formating.common_json_stylish import generate_json_stylish
from gendiff.formating.converters import convert_for_stylish


def generate_stylish(comparison):
    converter = convert_for_stylish
    return generate_json_stylish(comparison, converter)
