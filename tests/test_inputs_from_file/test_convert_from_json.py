import gendiff.inputs_from_file.convert_from_json as conv


def test_load_json(get_test_data):
    assert conv.load_json("") == {}
    normalized_paths, data_and_results = get_test_data
    for index, value in enumerate(normalized_paths):
        if value[0].lower().endswith('.json'):
            assert conv.load_json(value[0]) == data_and_results[index][0]
        if value[1].lower().endswith('.json'):
            assert conv.load_json(value[1]) == data_and_results[index][1]
