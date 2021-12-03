import sys
import gendiff.scripts.launch_script as scr
import argparse


ARGUMENT1 = 'first_file'
ARGUMENT2 = 'second_file'


def test_prepare_argparse_object():
    parser = scr.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
    args = parser.parse_args([ARGUMENT1, ARGUMENT2])
    assert args.first_file == ARGUMENT1
    assert args.second_file == ARGUMENT2


def test_main(get_test_data):
    normalized_paths, _ = get_test_data
    for value in normalized_paths:
        sys.argv = ["test", value[0], value[1]]
        assert scr.main() is None
