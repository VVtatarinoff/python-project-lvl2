#!/usr/bin/env python3
import argparse

import gendiff.gendiff as g
from gendiff.formating.format_report import CHOICES


ARGUMENTS = [
    [('-f', '--format'), {'metavar': 'FORMAT', 'help': 'set format of output',
                          'default': None, "choices": list(CHOICES.keys())}],
    [('first_file', ), {}],
    [('second_file', ), {}],
]


def prepare_argparse_object():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')
    for argument in ARGUMENTS:
        parser.add_argument(*argument[0], **argument[1])
    return parser


def main():
    args = prepare_argparse_object().parse_args()
    report = g.generate_diff(args.first_file, args.second_file, args.format)
    print(report)


if __name__ == '__main__':
    main()
