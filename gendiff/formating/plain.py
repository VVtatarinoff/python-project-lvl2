from itertools import chain

from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT
from gendiff.compare_data.comparison_tree import SPLIT, CHANGED
from gendiff.compare_data.comparison_tree import STATUS, VALUE
from gendiff.compare_data.comparison_tree import VALUE_INITIAL
from gendiff.compare_data.comparison_tree import VALUE_MODIFIED

from gendiff.formating.suplementary import convert_non_string as converter


RENAME_DICT = {ADD: "Property '{0}' was added with value: {1}",
               DEL: "Property '{0}' was removed"}
UPDATED = "Property '{0}' was updated. From {1} to {2}"


def convert_value(argument):
    complex_formats = [list, dict, set, tuple]
    if isinstance(argument, str):
        return f"'{argument}'"
    if type(argument) in complex_formats:
        return "[complex value]"
    return str(converter(argument))


def opposite_case(sign, value):
    opposite_signs = {ADD: DEL, DEL: ADD}
    if sign in opposite_signs:
        return (value, opposite_signs[sign])
    return (value, object())


def walker(data, pedigree=[]):
    line = []
    for name, match in data.items():
        status = match[STATUS]
        if status == KEPT:
            continue
        parent = pedigree + [name]
        full_name = ".".join(parent)
        if status == SPLIT:
            line += chain(walker(match[VALUE], parent))
        elif status == CHANGED:
            deleted = convert_value(match[VALUE_INITIAL])
            changed = convert_value(match[VALUE_MODIFIED])
            line.append(UPDATED.format(full_name, deleted, changed))
        else:
            changed = convert_value(match[VALUE])
            line.append(RENAME_DICT[status].format(full_name, changed))
    return line


def generate_plain(data):
    lines = walker(data)
    return '\n'.join(lines)
