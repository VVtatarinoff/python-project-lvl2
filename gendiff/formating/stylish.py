import json
from itertools import chain


def generate_stylish(comparison, depth=0, supress_sign=None):
    CHAR = " "
    COUNT_CHARS = 2
    if not isinstance(comparison, dict):
        if not isinstance(comparison, str):
            return json.JSONEncoder().encode(comparison)
        return comparison
    normal_indent = COUNT_CHARS * (1 + depth) * CHAR
    additional_space = CHAR * 2 * depth
    deep_indent = normal_indent + additional_space
    current_indent = CHAR * depth * COUNT_CHARS + additional_space
    lines = []
    for key, value in comparison.items():
        sign = key[1] if not supress_sign else supress_sign
        further_supress = " " if sign in {'-', '+', ' '} else None
        if sign == '?':
            sign = ' '
        indent = deep_indent + sign + CHAR
        converted_value = generate_stylish(value,
                                           depth + 1,
                                           further_supress)
        lines.append(f'{indent}{key[0]}: {converted_value}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
