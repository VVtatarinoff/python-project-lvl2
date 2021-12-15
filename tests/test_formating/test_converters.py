import gendiff.formating.suplementary as cv


def test_convert_non_string_bool():
    assert cv.convert_non_string(True) == 'true'
    assert cv.convert_non_string(False) == 'false'


def test_convert_non_string_others():
    assert cv.convert_non_string(None) == 'null'
    assert cv.convert_non_string("Text") == 'Text'
    assert cv.convert_non_string(10) == '10'
