import os
import sys

import argparse
import json
from .prepare_test_data import get_test_data
import gendiff.generate_diff as gen


normalized_paths, data_and_results = get_test_data()


def test_generate_report():
    for index, value in enumerate(normalized_paths):
        assert gen.generate_report(value[0], value[1]) == data_and_results[index][2]
