import json

import argparse


ARGUMENTS = [
    ['-f, -format', {'metavar': 'Format', 'help': 'set format of output'}],
    ['first_file', {}],
    ['second_file', {}],
]


def prepare_argparse_object():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')
    for argument in ARGUMENTS:
        parser.add_argument(argument[0], **argument[1])
    return parser


def get_data_from_json(file_name):
    with open(file_name, mode='r') as file:
        args_dict = json.load(file)
    return args_dict


def line_difference(args, char=" ", count_char=2, depth=0):
    block = ""
    tab = char * count_char * (1 + depth)
    for line in args:
        block += f"{tab}{line[0]} {line[1]}: {line[2]}\n"
    return block


def generate_diff():
    args = prepare_argparse_object().parse_args()
    first_arguments = get_data_from_json(args.first_file)
    second_arguments = get_data_from_json(args.second_file)
    keys = sorted(list(first_arguments.keys() | second_arguments.keys()))
    differences = "{\n"
    for key in keys:
        if key not in first_arguments:
            block = [['+', key, second_arguments[key]]]
        elif key not in second_arguments:
            block = [['-', key, first_arguments[key]]]
        elif first_arguments[key] == second_arguments[key]:
            block = [[' ', key, first_arguments[key]]]
        else:
            block = [['-', key, first_arguments[key]]]
            block += [['+', key, second_arguments[key]]]
        differences += line_difference(block)
    differences += '}'
    print(differences)
    return differences
