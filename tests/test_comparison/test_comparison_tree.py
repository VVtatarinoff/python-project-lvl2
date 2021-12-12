from gendiff.compare_data.comparison_tree import\
    create_comparison_tree as compare_tree


def test_parse_data(get_raw_data, get_mergings):
    assert compare_tree({}, {}) == {}
    complexity, merging = get_mergings
    path1 = get_raw_data[complexity + '1']
    path2 = get_raw_data[complexity + '2']
    result_of_merging = compare_tree(path1, path2)
    assert merging == result_of_merging
