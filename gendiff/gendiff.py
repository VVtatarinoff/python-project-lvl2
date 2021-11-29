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
    if not file_name:
        return {}
    with open(file_name, mode='r') as file:
        args_dict = json.load(file)
    return args_dict


def generate_difference_line(args, char=" ", count_char=2, depth=0):
    if not args:
        return ""
    block = ""
    tab = char * count_char * (1 + depth)
    for line in args:
        if line:
            block += f"{tab}{line[0]} {line[1]}: {line[2]}\n"
    return block


def generate_difference_report(initial, modified, char=" ",
                               count_char=2, depth=0):
    zero_tab = char * count_char * depth
    report = zero_tab + "{\n"
    keys = sorted(list(initial.keys() | modified.keys()))
    for key in keys:
        if key not in initial:
            block = [['+', key, modified[key]]]
        elif key not in modified:
            block = [['-', key, initial[key]]]
        elif initial[key] == modified[key]:
            block = [[' ', key, initial[key]]]
        else:
            block = [['-', key, initial[key]]]
            block += [['+', key, modified[key]]]
        report += generate_difference_line(block, char, count_char, depth)
    report += zero_tab + '}'
    return report


def generate_diff():
    args = prepare_argparse_object().parse_args()
    first_arguments = get_data_from_json(args.first_file)
    second_arguments = get_data_from_json(args.second_file)
    differences = generate_difference_report(first_arguments, second_arguments)
    print(differences)
    return differences
