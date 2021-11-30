import json
import yaml


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_json(json_file):
    if not json_file:
        return {}
    with open(json_file) as file:
        return json.load(file)


def load_yaml(yml_file):

    if not yml_file:
        return {}
    with open(yml_file) as file:
        data = file.read()
        return yaml.load(data, Loader=Loader)


def extract_raw_data(file):
    if file.lower().endswith('.json'):
        return load_json(file)
    elif any([file.lower().endswith('.yaml'),
             file.lower().endswith('.yml')]):
        return load_yaml(file)
