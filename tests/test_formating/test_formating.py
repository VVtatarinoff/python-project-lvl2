from gendiff.formating.json import generate_json as js
from gendiff.formating.plain import generate_plain as pl
from gendiff.formating.stylish import generate_stylish as stl
import pytest


@pytest.mark.parametrize("styles", [('json', js), ('plain', pl),
                                    ('stylish', stl)])
def test_generate_format(styles, get_reports, get_mergings):
    style, func = styles
    assert func({}) == ""
    style_reports = get_reports[style]
    for complexity, expected_report in style_reports.items():
        generated_report = func(get_mergings[complexity])
        assert expected_report == generated_report
