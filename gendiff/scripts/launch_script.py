#!/usr/bin/env python3
import gendiff.generate_diff as g
import argparse


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


def main():
    args = prepare_argparse_object().parse_args()
    report = g.generate_report(args.first_file, args.second_file)
    print(report)


if __name__ == '__main__':
    main()
