import gendiff.inputs_from_file.convert_from_file as conv
from tests.prepare_test_data import get_test_data

normalized_paths, data_and_results = get_test_data()


def test_extract_raw_data():
    assert conv.extract_raw_data('') == {}
    for index, value in enumerate(normalized_paths):
        assert conv.extract_raw_data(value[0]) == data_and_results[index][0]
        assert conv.extract_raw_data(value[1]) == data_and_results[index][1]
