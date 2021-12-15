from gendiff.inputs_from_file.convert_from_file import\
    extract_raw_data


def test_load_data(complexity_and_file, raw_data):
    test_data_variant, path_to_source_file = complexity_and_file
    result_of_load = extract_raw_data(path_to_source_file)
    result_expected = raw_data[test_data_variant]
    assert result_expected == result_of_load
