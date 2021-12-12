import gendiff.gendiff as gen
import pytest


@pytest.mark.parametrize("style", ['stylish', 'plain', 'json'])
def test_generate_report(get_complexity_pair_files, get_reports, style):
    complexity, file1, file2 = get_complexity_pair_files
    report = get_reports[style][complexity]
    assert gen.generate_diff(file1, file2, style) == report
