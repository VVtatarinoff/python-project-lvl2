from gendiff.formating.json import generate_json as js
from gendiff.formating.plain import generate_plain as pl
from gendiff.formating.stylish import generate_stylish as stl
import pytest


@pytest.mark.parametrize("variant", ['plain', 'complex',
                                     'hexlet'])
@pytest.mark.parametrize("styles", [('json', js), ('plain', pl),
                                    ('stylish', stl)])
def test_generate_format(styles, variant, reports, merging_versions):
    style, func = styles
    assert func({}) == ""
    expected_report = reports[style][variant]
    generated_report = func(merging_versions[variant])
    assert expected_report == generated_report
