import gendiff.gendiff as gen
import pytest


@pytest.mark.parametrize("style", ['stylish', 'plain', 'json'])
def test_generate_report(complexity_pair_files, reports, style):
    variant_of_report,\
        path_to_source_file1,\
        path_to_source_file2 = complexity_pair_files

    expected_report = reports[style][variant_of_report]
    generated_report = gen.generate_diff(path_to_source_file1,
                                         path_to_source_file2,
                                         style)
    assert generated_report == expected_report
