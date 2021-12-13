from gendiff.formating.converters import convert_stylish as converter
from itertools import chain

from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT, SPLIT

SIGNS = {ADD: '+',
         DEL: '-',
         KEPT: ' ',
         SPLIT: ' '}


def generate_report(comparison, depth=0, supress_sign=None):
    CHAR = " "
    COUNT_CHARS = 2
    if not isinstance(comparison, dict):
        return converter(comparison)
    normal_indent = COUNT_CHARS * (1 + depth) * CHAR
    additional_space = CHAR * 2 * depth
    deep_indent = normal_indent + additional_space
    current_indent = CHAR * depth * COUNT_CHARS + additional_space
    lines = []
    for key, value in comparison.items():
        sign = key[1] if not supress_sign else supress_sign
        further_supress = KEPT if sign in {DEL, ADD, KEPT} else None
        output_key = converter(key[0]) if not supress_sign else converter(key)
        indent = deep_indent + SIGNS[sign] + CHAR
        converted_value = generate_report(value,
                                          depth + 1,
                                          further_supress)
        lines.append(f'{indent}{output_key}: {converted_value}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def generate_stylish(comparison):
    if not comparison:
        return ""
    return generate_report(comparison)
