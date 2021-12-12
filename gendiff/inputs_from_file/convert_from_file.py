import gendiff.inputs_from_file.convert_from_json as js
import gendiff.inputs_from_file.convert_from_yaml as yml

CONVERTERS = {
    '.json': js.load_json,
    '.yaml': yml.load_yaml,
    '.yml': yml.load_yaml}


def extract_raw_data(file):
    if not file:
        return {}
    path = file.lower()
    with open(file) as f:
        data = f.read()
    for key in CONVERTERS:
        if path.endswith(key):
            return CONVERTERS[key](data)
