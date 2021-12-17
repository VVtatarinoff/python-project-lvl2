from gendiff.formating.suplementary import convert_non_string as converter
from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT
from gendiff.compare_data.comparison_tree import SPLIT, CHANGED
from gendiff.compare_data.comparison_tree import STATUS, VALUE
from gendiff.compare_data.comparison_tree import VALUE_INITIAL
from gendiff.compare_data.comparison_tree import VALUE_MODIFIED

SIGNS = {ADD: '+ ',
         DEL: '- ',
         KEPT: '  ',
         CHANGED: '+-'}

STRING = "{0}{1}: {2}"

ZERO_INDENT = 4
SIGN_INDENT = 2


def is_dict(argument):
    return isinstance(argument, dict)


def converter_value(source, indent):
    lines = []
    for key, value in source.items():
        if is_dict(value):
            current_line = [STRING.format(indent, key, "{")]
            current_line += converter_value(value, indent + ZERO_INDENT * " ")
        else:
            current_line = [STRING.format(indent, key, converter(value))]
        lines += current_line
    lines.append(indent[:-ZERO_INDENT] + '}')
    return lines


def generate_report(data, depth=0):
    lines = []
    indent = ' ' * (depth * ZERO_INDENT + SIGN_INDENT)
    for key, match in data.items():
        status = match[STATUS]
        if status == SPLIT:
            deep_lines = generate_report(match[VALUE], depth + 1)
            lines.append(STRING.format(indent + ' ' * SIGN_INDENT, key, '{'))
            lines += deep_lines
            continue
        if status == CHANGED:
            values = {SIGNS[DEL]: match[VALUE_INITIAL],
                      SIGNS[ADD]: match[VALUE_MODIFIED]}
        else:
            values = {SIGNS[status]: match[VALUE]}
        for sign, value in values.items():
            if is_dict(value):
                lines.append(STRING.format(indent + sign, key, '{'))
                deep_indent = indent + (ZERO_INDENT + 2) * " "
                deep_lines = converter_value(value, deep_indent)
                lines += deep_lines
            else:
                lines.append(STRING.format(indent + sign,
                                           key,
                                           converter(value)))
    lines.append(indent[:-SIGN_INDENT] + '}')
    return lines


def generate_stylish(comparison):
    if not comparison:
        return ""
    lines = ['{'] + generate_report(comparison)
    return '\n'.join(lines)
