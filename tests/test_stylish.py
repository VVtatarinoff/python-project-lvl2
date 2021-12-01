import gendiff.formating.stylish as styl
from tests.prepare_test_data import PLAIN1, PLAIN2, COMPLEX1, COMPLEX2, PLAIN_COMPARE, COMPLEX_COMPARE
from tests.prepare_test_data import get_test_data



def test_generate_stylish():
    _, data_and_results = get_test_data()
    assert styl.generate_stylish({}) == '{\n}'
    assert styl.generate_stylish(PLAIN_COMPARE) == data_and_results[0][2]
    assert styl.generate_stylish(COMPLEX_COMPARE) == data_and_results[1][2]