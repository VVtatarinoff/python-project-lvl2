import gendiff.parsing.parsing as pars


def test_parse_data():
    arg1 = {}
    arg2 = {}
    assert pars.parse_data(arg1, arg2) == {}
    arg2 = {'abc': 3}
    assert pars.parse_data(arg1, arg2) == {('abc', '+'): 3}


def test_parse_data_plain_work(get_plain_source_patterns, get_plain_merging):
    plain1, plain2 = get_plain_source_patterns
    assert pars.parse_data(plain1, plain2) == get_plain_merging


def test_parse_data_complex_work(get_complex_source_patterns,
                                 get_complex_merging):
    complex1, complex2 = get_complex_source_patterns
    assert pars.parse_data(complex1, complex2) == get_complex_merging
