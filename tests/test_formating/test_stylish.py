import gendiff.formating.stylish as styl


def test_generate_stylish(get_test_data,
                          get_plain_merging,
                          get_complex_merging):
    _, data_and_results = get_test_data
    assert styl.generate_stylish({}) == '{\n}'
    assert styl.generate_stylish(get_plain_merging) == data_and_results[0][2]
    assert styl.generate_stylish(get_complex_merging) == data_and_results[1][2]
