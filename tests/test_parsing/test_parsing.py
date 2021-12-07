from gendiff.parsing.parsing import parse_data as pars


def test_parse_data(get_raw_data, get_mergings):
    assert pars({}, {}) == {}
    for complexity, merging in get_mergings.items():
        path1 = get_raw_data[complexity + '1']
        path2 = get_raw_data[complexity + '2']
        result_of_merging = pars(path1, path2)
        assert merging == result_of_merging
