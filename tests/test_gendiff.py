import gendiff.gendiff as gen
import pytest


@pytest.mark.parametrize("style", ['stylish', 'plain', 'json'])
def test_generate_report(get_source_files, get_reports, style):
    for pair in get_source_files:
        files = tuple()
        for key, path in pair.items():
            complexity = key[:-1]
            files += (path,)
        report = get_reports[style][complexity]
        print(report)
        print(style)
        print(*files)
        assert gen.generate_diff(*files, style) == report
