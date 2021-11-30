import argparse
import json

from gendiff.parsing import parse_data

ARGUMENTS = [
    [('-f', '--format'), {'metavar': 'FORMAT', 'help': 'set format of output'}],
    [('first_file', ), {}],
    [('second_file', ), {}],
]


def prepare_argparse_object():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')
    for argument in ARGUMENTS:
        parser.add_argument(*argument[0], **argument[1])
    return parser


def get_data_from_json(file_name):
    if not file_name:
        return {}
    with open(file_name, mode='r') as file:
        args_dict = json.load(file)
    return args_dict

def get_data_from_yaml(file_name):
    pass


def generate_diff():
    args = prepare_argparse_object().parse_args()
    first_arguments = get_data_from_json(args.first_file)
    second_arguments = get_data_from_json(args.second_file)
    parsed_data = parse_data(first_arguments, second_arguments)
    return parsed_data