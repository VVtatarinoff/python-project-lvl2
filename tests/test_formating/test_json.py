import gendiff.formating.json as js


def test_generate_json(get_test_data, get_plain_merging, get_complex_merging):
    _, data_and_results = get_test_data
    assert js.generate_json({}) == "{}"
    assert js.generate_json(get_plain_merging) == data_and_results[0][4]
    assert js.generate_json(get_complex_merging) == data_and_results[1][4]
