import yaml


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_yaml(data):
    return yaml.load(data, Loader=Loader)
