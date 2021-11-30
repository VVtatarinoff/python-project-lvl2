import os
import sys

import argparse
import json

import gendiff.generate_diff as gen
import gendiff.parsing as prs

FILES_AND_RESULTS = [['test01.json', 'test02.json', 'result00.txt'],
                     ['test11.json', 'test12.json', 'result01.txt']]
ARGUMENT1 = 'first_file'
ARGUMENT2 = 'second_file'


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


normalized_paths = []
data_and_results = []
for check_data in FILES_AND_RESULTS:
    normalized_paths.append([get_fixture_path(check_data[0]),
                             get_fixture_path(check_data[1]),
                             get_fixture_path(check_data[2])])
    with open(normalized_paths[-1][0]) as file1:
        with open(normalized_paths[-1][1]) as file2:
            with open(normalized_paths[-1][2]) as file3:
                json1 = json.load(file1)
                json2 = json.load(file2)
                result = file3.read()
                data_and_results.append([json1, json2, result])


def test_prepare_argparse_object():
    parser = gen.prepare_argparse_object()
    assert isinstance(parser, argparse.ArgumentParser)
    args = parser.parse_args([ARGUMENT1, ARGUMENT2])
    assert args.first_file == ARGUMENT1
    assert args.second_file == ARGUMENT2


def test_get_data_from_json():
    assert gen.get_data_from_json("") == {}
    for index, value in enumerate(normalized_paths):
        assert gen.get_data_from_json(value[0]) == data_and_results[index][0]
        assert gen.get_data_from_json(value[1]) == data_and_results[index][1]


def test_generate_diff():
    for index, value in enumerate(normalized_paths):
        sys.argv = ["test", value[0], value[1]]
        assert gen.generate_diff() == data_and_results[index][2]
