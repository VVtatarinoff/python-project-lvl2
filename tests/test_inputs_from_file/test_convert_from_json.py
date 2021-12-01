import gendiff.inputs_from_file.convert_from_json as conv
from tests.prepare_test_data import get_test_data

normalized_paths, data_and_results = get_test_data()


def test_load_json():
    assert conv.load_json("") == {}
    for index, value in enumerate(normalized_paths):
        if value[0].lower().endswith('.json'):
            assert conv.load_json(value[0]) == data_and_results[index][0]
        if value[1].lower().endswith('.json'):
            assert conv.load_json(value[1]) == data_and_results[index][1]
