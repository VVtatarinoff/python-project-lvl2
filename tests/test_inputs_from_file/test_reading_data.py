from gendiff.inputs_from_file.convert_from_yaml import load_yaml as yml
from gendiff.inputs_from_file.convert_from_json import load_json as js
from gendiff.inputs_from_file.convert_from_file import\
    extract_raw_data as common
import pytest


@pytest.mark.parametrize("types", [('json', js), ('yaml', yml),
                                   ('yml', yml), ('', common)])
def test_load_data(types, get_source_files, get_raw_data):
    file_type, func = types
    assert func('') == {}
    for pair in get_source_files:
        for complexity, path in pair.items():
            if path.endswith(file_type):
                result_of_load = func(path)
                result_expected = get_raw_data[complexity]
                assert result_expected == result_of_load
