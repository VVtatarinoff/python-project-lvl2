import json


def load_json(json_file):
    if not json_file:
        return {}
    with open(json_file) as file:
        return json.load(file)
