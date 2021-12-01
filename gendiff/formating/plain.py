from itertools import chain


RENAME_DICT = {'+': "Property '{0}' was added with value: {1}",
               '-': "Property '{0}' was removed"}
UPDATED = "Property '{0}' was updated. From {1} to {2}"


def is_dict(argument):
    return isinstance(argument, dict)


def convert_value(argument):
    replacements = {True: 'true', False: 'false', None: 'null'}
    complex_formats = [list, dict, set, tuple]
    if isinstance(argument, str):
        return f"'{argument}'"
    if type(argument) in complex_formats:
        return "[complex value]"
    if argument in replacements:
        return replacements[argument]
    return str(argument)


def opposite_case(sign, value):
    if sign == '+':
        return (value, '-')
    if sign == '-':
        return (value, '+')
    return (value, 'None')


def walker(data, pedigree=[]):
    line = []
    for key, value in data.items():
        sign = key[1]
        if sign == ' ':
            continue
        name = key[0]
        parent = pedigree + [name]
        full_name = ".".join(parent)
        opposite = opposite_case(sign, name)
        changed = convert_value(value)
        if opposite in data:
            if sign == '+':
                deleted = convert_value(data[opposite])
                line.append(UPDATED.format(full_name, deleted, changed))
            continue
        if sign == "?":
            line += chain(walker(value, parent))
        else:
            line.append(RENAME_DICT[sign].format(full_name, changed))
    return line


def generate_plain(data):
    lines = walker(data)
    return '\n'.join(lines)