import json
from itertools import chain


def generate_json_report(comparison, depth=0, supress_sign=None):
    CHAR = " "
    COUNT_CHARS = 2
    if not isinstance(comparison, dict):
        if not isinstance(comparison, str):
            return json.JSONEncoder().encode(comparison)
        return comparison
    normal_indent = COUNT_CHARS * (1 + depth) * CHAR
    additional_space = CHAR * 2 * depth
    deep_indent = normal_indent  + additional_space
    current_indent = CHAR * depth * COUNT_CHARS + additional_space
    lines = []
    for key, value in comparison.items():
        sign = key[1] if not supress_sign else supress_sign
        further_supress = " " if sign in {'-', '+', ' '} else None
        if sign == '?':
            sign = ' '
        indent = deep_indent + sign + CHAR
        converted_value = generate_json_report(value,
                                               depth + 1,
                                               further_supress)
        lines.append(f'{indent}{key[0]}: {converted_value}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def get_differences(arg1, arg2): # noqa C901
    if not isinstance(arg1, dict):
        return arg1
    if not isinstance(arg2, dict):
        return arg2
    keys = sorted(list(arg1.keys() | arg2.keys()))
    if not keys:
        return {}
    dif_dict = {}
    for key in keys:
        if key not in arg1:
            dif_dict[(key, '+')] = get_differences({}, arg2[key])
        elif key not in arg2:
            dif_dict[(key, '-')] = get_differences(arg1[key], {})
        elif arg1[key] == arg2[key]:
            dif_dict[(key, ' ')] = get_differences(arg1[key], arg2[key])
        else:
            if isinstance(arg1[key], dict) and isinstance(arg2[key], dict):
                dif_dict[(key, "?")] = get_differences(arg1[key], arg2[key])
            else:
                dif_dict[(key, '-')] = get_differences(arg1[key], {})
                dif_dict[(key, '+')] = get_differences({}, arg2[key])
    return dif_dict


def parse_data(initial_data, modified_data):
    diff = get_differences(initial_data, modified_data)
    report = generate_json_report(diff)
    print(report)
    return report
