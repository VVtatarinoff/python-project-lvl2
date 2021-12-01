import yaml


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_yaml(yml_file):
    if not yml_file:
        return {}
    with open(yml_file) as file:
        data = file.read()
        return yaml.load(data, Loader=Loader)
