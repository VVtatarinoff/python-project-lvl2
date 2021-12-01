import gendiff.parsing.parsing as pars
from tests.prepare_test_data import PLAIN1, PLAIN2
from tests.prepare_test_data import COMPLEX1, COMPLEX2
from tests.prepare_test_data import PLAIN_COMPARE, COMPLEX_COMPARE


def test_parse_data():
    arg1 = {}
    arg2 = {}
    assert pars.parse_data(arg1, arg2) == {}
    arg2 = {'abc': 3}
    assert pars.parse_data(arg1, arg2) == {('abc', '+'): 3}
    assert pars.parse_data(PLAIN1, PLAIN2) == PLAIN_COMPARE
    assert pars.parse_data(COMPLEX1, COMPLEX2) == COMPLEX_COMPARE
