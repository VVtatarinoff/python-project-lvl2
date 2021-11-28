import json

import argparse


def set_argparse_object():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '-format', metavar='FORMAT',
                        help='set format of output')
    return parser


def get_data_from_json(file_name):
    with open(file_name, mode='r') as file:
        args_dict = json.load(file)
    return args_dict


def line_difference(sign, key, value):
    return f"  {sign} {key}: {value}\n"


def generate_diff():
    parser = set_argparse_object()
    args = parser.parse_args()
    first_arguments = get_data_from_json(args.first_file)
    second_arguments = get_data_from_json(args.second_file)
    keys = sorted(list(first_arguments.keys() | second_arguments.keys()))
    differences = "{\n"
    for key in keys:
        if key not in first_arguments:
            differences += line_difference('+', key, second_arguments[key])
        elif key not in second_arguments:
            differences += line_difference('-', key, first_arguments[key])
        elif first_arguments[key] == second_arguments[key]:
            differences += line_difference(' ', key, first_arguments[key])
        else:
            differences += line_difference('-', key, first_arguments[key])
            differences += line_difference('+', key, second_arguments[key])
    differences += '}'
    print(differences)
    return differences
