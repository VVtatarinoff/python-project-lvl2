from itertools import chain

from gendiff.formating.suplementary import convert_non_string as converter
from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT
from gendiff.compare_data.comparison_tree import SPLIT, CHANGED
from gendiff.compare_data.comparison_tree import STATUS, VALUE
from gendiff.compare_data.comparison_tree import VALUE_INITIAL
from gendiff.compare_data.comparison_tree import VALUE_MODIFIED

SIGNS = {ADD: '+',
         DEL: '-',
         KEPT: ' ',
         SPLIT: ' ',
         CHANGED: '+-'}

STRING = "{0}{1}: {2}"


def is_dict(argument):
    return isinstance(argument, dict)


def generate_normal_lines(current_value, depth, spaces_count, replacer=" "):
    if not is_dict(current_value):
        return converter(current_value)
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * depth
    lines = []
    for key, val in current_value.items():
        next_lines = generate_normal_lines(val,
                                           deep_indent_size,
                                           spaces_count)
        lines.append(f'{deep_indent}{key}: {next_lines}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def generate_report(comparison, depth=0):
    CHAR = " "
    COUNT_CHARS = 2
    normal_indent = COUNT_CHARS * (1 + depth) * CHAR
    additional_space = CHAR * 2 * depth
    deep_indent = normal_indent + additional_space
    current_indent = CHAR * depth * COUNT_CHARS + additional_space
    lines = []
    for name, match in comparison.items():
        status = match[STATUS]
        if status == SPLIT:
            sign = SIGNS[status]
            indent = deep_indent + sign + CHAR
            further_lines = generate_report(match[VALUE], depth + 1)
            lines.append(STRING.format(indent, name, further_lines))
            continue
        if status == CHANGED:
            values = {DEL: match[VALUE_INITIAL], ADD: match[VALUE_MODIFIED]}
        else:
            values = {status: match[VALUE]}
        for sign, value in values.items():
            indent = deep_indent + SIGNS[sign] + CHAR
            if is_dict(value):
                further_lines = generate_normal_lines(value,
                                                      len(indent),
                                                      (COUNT_CHARS + 2),
                                                      CHAR)
            else:
                further_lines = converter(value)
            lines.append(STRING.format(indent, name, further_lines))
        result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def generate_stylish(comparison):
    if not comparison:
        return ""
    return generate_report(comparison)
