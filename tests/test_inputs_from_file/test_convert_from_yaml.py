import gendiff.inputs_from_file.convert_from_yaml as conv


def test_load_yaml(get_test_data):
    assert conv.load_yaml("") == {}
    normalized_paths, data_and_results = get_test_data
    for index, value in enumerate(normalized_paths):
        name = value[0].lower()
        if name.endswith('.yml') or name.endswith('.yaml'):
            assert conv.load_yaml(value[0]) == data_and_results[index][0]
        if name.endswith('.yml') or name.endswith('.yaml'):
            assert conv.load_yaml(value[1]) == data_and_results[index][1]
