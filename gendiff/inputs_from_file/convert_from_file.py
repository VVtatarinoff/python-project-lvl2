import gendiff.inputs_from_file.convert_from_json as js
import gendiff.inputs_from_file.convert_from_yaml as yml

CONVERTERS = {
    '.json': js.load_json,
    '.yaml': yml.load_yaml,
    '.yml': yml.load_yaml}


def extract_raw_data(file):
    path = file.lower()
    for key in CONVERTERS:
        if path.endswith(key):
            return CONVERTERS[key](file)
    return {}
