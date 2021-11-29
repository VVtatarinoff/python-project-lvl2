import sys

import argparse

import gendiff.gendiff as g

FIRST_FILE = 'gendiff/tests/fixtures/file1.json'
SECOND_FILE = 'gendiff/tests/fixtures/file2.json'
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


def test_prepare_argparse_object():
    parser = g.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
    args = parser.parse_args([FIRST_FILE, SECOND_FILE])
    assert args.first_file == FIRST_FILE
    assert args.second_file == SECOND_FILE


def test_get_data_from_json():
    assert g.get_data_from_json("") == {}
    assert g.get_data_from_json(FIRST_FILE) == FIRST_DATA
    assert g.get_data_from_json(SECOND_FILE) == SECOND_DATA


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
    sys.argv = ["test", FIRST_FILE, SECOND_FILE]
    assert g.generate_diff() == DIFF_REPORT
