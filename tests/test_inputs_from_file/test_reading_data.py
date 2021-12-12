from gendiff.inputs_from_file.convert_from_file import\
    extract_raw_data


def get_extension(file):
    return file.split('.')[-1]


def test_load_data(get_complexity_and_file, get_raw_data):
    complexity, path = get_complexity_and_file
    result_of_load = extract_raw_data(path)
    result_expected = get_raw_data[complexity]
    assert result_expected == result_of_load
