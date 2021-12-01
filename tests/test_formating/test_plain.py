import gendiff.formating.plain as pl
from tests.prepare_test_data import PLAIN_COMPARE, COMPLEX_COMPARE
from tests.prepare_test_data import get_test_data


def test_generate_plain():
    _, data_and_results = get_test_data()
    assert pl.generate_plain({}) == ""
    assert pl.generate_plain(PLAIN_COMPARE) == data_and_results[0][3]
    assert pl.generate_plain(COMPLEX_COMPARE) == data_and_results[1][3]
