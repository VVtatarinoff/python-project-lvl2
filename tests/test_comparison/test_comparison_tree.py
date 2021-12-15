from gendiff.compare_data.comparison_tree import\
    create_comparison_tree as compare_tree


def test_comparisons_of_datas(raw_data, mergings):
    assert compare_tree({}, {}) == {}
    test_data_variant, expected_comparison = mergings
    data_from_file1 = raw_data[test_data_variant + '1']
    data_from_file2 = raw_data[test_data_variant + '2']
    result_of_merging = compare_tree(data_from_file1, data_from_file2)
    assert expected_comparison == result_of_merging
