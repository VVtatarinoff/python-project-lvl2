import gendiff.formating.json as js
from tests.prepare_test_data import PLAIN_COMPARE, COMPLEX_COMPARE
from tests.prepare_test_data import get_test_data



def test_generate_json():
    _, data_and_results = get_test_data()
    assert js.generate_json({}) == '{\n}'
    assert js.generate_json(PLAIN_COMPARE) == data_and_results[0][4]
    assert js.generate_json(COMPLEX_COMPARE) == data_and_results[1][4]