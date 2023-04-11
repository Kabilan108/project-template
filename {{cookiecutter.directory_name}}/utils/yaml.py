"""Contain Common Utilies."""
from __future__ import absolute_import, print_function

import os

import yaml


def read_yaml(filepath: str) -> object:
    """Read yaml file and pass python object.
    Args:
        filepath (str): path to yaml file.
    Returns:
        object: python object.
    """
    with open(filepath, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return data


def write_yaml(filepath: str, data: object) -> None:
    """Write yaml file from dict.
    Args:
        filepath (str): path for yaml file.
        arg_dict (Dict): dictionary with arguments.
    """
    yaml_dir = os.path.dirname(filepath)
    os.makedirs(yaml_dir, exist_ok=True)

    with open(filepath, "w") as outfile:
        yaml.dump(data, outfile, default_flow_style=False)