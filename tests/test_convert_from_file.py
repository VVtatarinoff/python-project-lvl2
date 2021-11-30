import gendiff.convert_from_file as conv
from .prepare_test_data import get_test_data

import json
import yaml


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
normalized_paths, data_and_results = get_test_data()

def test_load_json():
    assert conv.load_json("") == {}
    for index, value in enumerate(normalized_paths):
        assert conv.load_json(value[0]) == data_and_results[index][0]
        assert conv.load_json(value[1]) == data_and_results[index][1]


def test_load_yaml():
    pass


def test_extract_raw_data():
    pass