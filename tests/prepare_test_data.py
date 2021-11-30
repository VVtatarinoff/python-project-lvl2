import os
import json

FILES_AND_RESULTS = [['test01.json', 'test02.json', 'result00.txt'],
                     ['test11.json', 'test12.json', 'result01.txt']]


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

def get_test_data():
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
    return normalized_paths, data_and_results