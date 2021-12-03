import gendiff.formating.plain as pl


def test_generate_plain(get_test_data, get_plain_merging, get_complex_merging):
    _, data_and_results = get_test_data
    assert pl.generate_plain({}) == ""
    assert pl.generate_plain(get_plain_merging) == data_and_results[0][3]
    assert pl.generate_plain(get_complex_merging) == data_and_results[1][3]
