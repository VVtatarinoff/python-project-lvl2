import argparse


def arg():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '-format', metavar='FORMAT',
                        help='set format of output')
    print(parser.parse_args())
