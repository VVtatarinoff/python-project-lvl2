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


def get_indent(depth):
    return ' ' * (depth * ZERO_INDENT + SIGN_INDENT)


def get_value_indent(depth):
    return ' ' * (depth * ZERO_INDENT + SIGN_INDENT * 2)


def convert_value(source, depth):
    if not is_dict(source):
        return converter(source)
    indent = get_value_indent(depth)
    lines = ['{']
    for key, value in source.items():
        current_line = [STRING.format(indent, key,
                                      convert_value(value,
                                                    depth + 1))]
        lines += current_line
    lines.append(get_value_indent(depth - 1) + '}')
    return '\n'.join(lines)


def generate_nodes(node, depth):
    indent = get_indent(depth)
    key, match = node
    status = match[STATUS]
    if status == SPLIT:
        return [STRING.format(indent + ' ' * SIGN_INDENT,
                              key, generate_stylish(match[VALUE],
                                                    depth + 1))]
    if status == CHANGED:
        values = {SIGNS[DEL]: match[VALUE_INITIAL],
                  SIGNS[ADD]: match[VALUE_MODIFIED]}
    else:
        values = {SIGNS[status]: match[VALUE]}
    lines = []
    for sign, value in values.items():
        line = STRING.format(indent + sign, key,
                             convert_value(value, depth + 1))
        lines.append(line)
    return lines


def generate_stylish(comparison, depth=0):
    if not comparison:
        return ""
    indent = get_indent(depth)
    lines = ['{']
    for node in comparison.items():
        line = generate_nodes(node, depth)
        lines += line
    indent_less_sign = indent[:-SIGN_INDENT]
    lines.append(indent_less_sign + '}')
    return '\n'.join(lines)
