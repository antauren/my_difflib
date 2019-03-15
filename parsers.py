import os

import yaml
import json


def parse(path):
    '''doc string'''  # TODO
    _, ext = os.path.splitext(path)

    ext = ext.lower()

    if ext in {'.yml', '.yaml'}:
        return yaml_load(path)

    elif ext in {'.json'}:
        return json_load(path)

    else:
        return None


def yaml_load(path):
    '''doc string'''  # TODO
    with open(path) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


def json_load(path):
    '''doc string'''  # TODO
    with open(path) as read_file:
        return json.load(read_file)
