import sys
import gendiff.scripts.launch_script as scr
import argparse
from tests.prepare_test_data import get_test_data

ARGUMENT1 = 'first_file'
ARGUMENT2 = 'second_file'

normalized_paths, _ = get_test_data()

def test_prepare_argparse_object():
    parser = scr.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
    args = parser.parse_args([ARGUMENT1, ARGUMENT2])
    assert args.first_file == ARGUMENT1
    assert args.second_file == ARGUMENT2


def test_main():
    for value in normalized_paths:
        sys.argv = ["test", value[0], value[1]]
        assert scr.main() == None
