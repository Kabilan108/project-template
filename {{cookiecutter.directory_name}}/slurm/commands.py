"""
Build string for passing to SLURM.
"""

from __future__ import absolute_import, print_function

from typing import Dict


def generic_arg_command(py_path: str, arg_dict: Dict) -> str:
    """
    Command with passing arguments.
    
    Parameters
    ----------
    py_path : str
        path to .py file to be executed.
    arg_dict : Dict 
        dictionary of arguments.

    Returns
    -------
    str
        command to be passed to SLURM.
    """
    arg_str = dict_to_str(arg_dict)
    return f"python {py_path} {arg_str}"


def generic_yaml_command(py_path: str, yaml_file: str) -> str:
    """
    Command with arguments in yaml file.

    Parameters
    ----------
    py_path : str
        path to .py file to be executed.
    yaml_file : str
        yaml file with arguments.

    Returns
    -------
    str
        command to be passed to SLURM.
    """
    return f"python {py_path} --config {yaml_file}"


def dict_to_str(_dict: Dict) -> str:
    """
    Convert dictionary to string.

    Parameters
    ----------
    _dict : Dict
        dictionary with arguments.

    Returns
    -------
    str
        arguments as string.
    """
    s = ""
    for k, v in _dict.items():
        s = s + k + " " + v + " "
    return s
