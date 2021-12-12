from gendiff.formating.json import generate_json as js
from gendiff.formating.plain import generate_plain as pl
from gendiff.formating.stylish import generate_stylish as stl
import pytest


@pytest.mark.parametrize("variants", ['plain', 'complex',
                                      'hexlet'])
@pytest.mark.parametrize("styles", [('json', js), ('plain', pl),
                                    ('stylish', stl)])
def test_generate_format(styles, variants, get_reports, merging_versions):
    style, func = styles
    assert func({}) == ""
    expected_report = get_reports[style][variants]
    generated_report = func(merging_versions[variants])
    assert expected_report == generated_report
