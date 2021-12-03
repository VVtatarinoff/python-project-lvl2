import gendiff.formating.converters as cv


def test_convert_stylish_bool():
    assert cv.convert_stylish(True) == 'true'
    assert cv.convert_stylish(False) == 'false'


def test_convert_stylish_others():
    assert cv.convert_stylish(None) == 'null'
    assert cv.convert_stylish("Text") == 'Text'
    assert cv.convert_stylish(10) == '10'
