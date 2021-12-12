import json

from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT, SPLIT

SIGNS = {ADD: '+',
         DEL: '-',
         KEPT: ' ',
         SPLIT: ' '}


def generate_report(comparison, supress_sign=None):
    if not isinstance(comparison, dict):
        return comparison
    result = {}
    for key, value in comparison.items():
        sign = key[1] if not supress_sign else supress_sign
        further_supress = KEPT if sign in {DEL, ADD, KEPT} else None
        next_value = generate_report(value,
                                     further_supress)
        result[SIGNS[sign] + " " + str(key[0])] = next_value
    return result


def generate_json(comparison):
    if not comparison:
        return ""
    result = generate_report(comparison)
    return json.dumps(result, sort_keys=True, indent=4)
