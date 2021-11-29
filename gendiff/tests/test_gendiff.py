import os
import sys

import argparse

import gendiff.gendiff as g

FIRST_FILE = 'file1test.json'
SECOND_FILE = 'file2test.json'
FIRST_DATA = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
             }  # noqa E126
SECOND_DATA = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
              }  # noqa E126
DIFF_REPORT = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

def test_prepare_argparse_object():
    parser = g.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
    args = parser.parse_args([FIRST_FILE, SECOND_FILE])
    assert args.first_file == FIRST_FILE
    assert args.second_file == SECOND_FILE


def test_get_data_from_json():
    assert g.get_data_from_json("") == {}
    assert g.get_data_from_json(get_fixture_path(FIRST_FILE)) == FIRST_DATA
    assert g.get_data_from_json(get_fixture_path(SECOND_FILE)) == SECOND_DATA


def test_generate_difference_line():
    args = [[1, 2, 3]]
    assert g.generate_difference_line([[]]) == ""
    assert g.generate_difference_line(args) == "  1 2: 3\n"
    assert g.generate_difference_line(args, "#") == "##1 2: 3\n"
    assert g.generate_difference_line(args, "#", count_char=4) == "####1 2: 3\n"
    expected = g.generate_difference_line(args, "#", count_char=2, depth=3)
    assert expected == "########1 2: 3\n"


def test_generate_difference_report():
    assert g.generate_difference_report({}, {}) == "{\n}"
    assert g.generate_difference_report(FIRST_DATA, SECOND_DATA) == DIFF_REPORT
    assert g.generate_difference_report({1: 2}, {1: 2}) == "{\n    1: 2\n}"
    expected = g.generate_difference_report({1: 2}, {1: 2}, char="#")
    assert expected == "{\n##  1: 2\n}"
    expected = g.generate_difference_report({1: 2}, {1: 2}, "#", 3)
    assert expected == "{\n###  1: 2\n}"
    expected = g.generate_difference_report({1: 2}, {1: 2}, "#", 3, 1)
    assert expected == "###{\n######  1: 2\n###}"


def test_generate_diff():
    file1 = get_fixture_path(FIRST_FILE)
    file2 = get_fixture_path(SECOND_FILE)
    sys.argv = ["test", file1, file2]
    assert g.generate_diff() == DIFF_REPORT
