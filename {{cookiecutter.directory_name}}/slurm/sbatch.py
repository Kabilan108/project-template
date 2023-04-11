"""
Send Job Arrays to SLURM.
"""

from __future__ import absolute_import, print_function

import os
import subprocess
from typing import Dict, List


def run_command(command: str) -> None:
    """
    Use subprocess to run a shell command.

    Parameters
    ----------
    command : str
        Command to run in the shell.

    Returns
    -------
    None
    """

    complete_process = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )

    if complete_process.check_returncode() is None:
        print(complete_process.stdout.decode("UTF-8"))
    else:
        print(complete_process.stderr.decode("UTF-8"))


def submit_array(
    root_dir: str,
    command_list: List,
    node_setting: str,
    job_name: str,
    conda_path: str = None,
) -> None:
    """
    Submit Job Arrays to SLURM.

    Parameters
    ----------
    root_dir : str
        Directory to write job arrays and shells.
    command_list : list
        List of commands to run in the job array.
    node_setting : str
        Settings for the compute node in the form of a string.
    job_name : str
        Name for the job.
    conda_path : str, optional
        Path to the conda environment. Defaults to None.

    Returns
    -------
    None
    """

    array_txt = os.path.join(root_dir, f"job_arrays/{job_name}.txt")
    write_array_txt(command_list, array_txt)

    num_jobs = len(command_list)
    node_setting = node_setting + f" --array=1-{num_jobs}%100"

    array_sh = os.path.join(root_dir, f"scripts/{job_name}.sh")
    write_shell(array_sh, node_setting, array_txt, conda_path)

    sbatch_command = f"sbatch {array_sh}"
    run_command(sbatch_command)


def write_array_txt(command_list: List, array_txt: str) -> None:
    """
    Write .txt for job arrays.

    Parameters
    ----------
    command_list : list
        List of commands to run in the job array.
    array_txt : str
        Path to the .txt file to be written.

    Returns
    -------
    None
    """

    array_dir = os.path.dirname(array_txt)
    os.makedirs(array_dir, exist_ok=True)

    with open(array_txt, "w") as f:
        for command in command_list:
            f.write(f"{command}\n")


def write_shell(
    array_sh: str, node_setting: Dict, array_txt: str, conda_path: str
) -> None:
    """
    Write shell for SLURM to run job arrays.

    Parameters
    ----------
    array_sh : str
        Path to the shell script to be written.
    node_setting : dict
        Dictionary containing SLURM settings for the compute node.
    array_txt : str
        Path to the text file containing the job array commands.
    conda_path : str
        Path to the Conda environment to be activated before running the job array (optional).

    Returns
    -------
    None
    """

    sh_dir = os.path.dirname(array_sh)
    os.makedirs(sh_dir, exist_ok=True)

    setting_list = node_setting.split(" ")
    with open(array_sh, "w") as f:
        f.write("#!/bin/bash \n")

        for i in setting_list:
            f.write(f"#SBATCH {i} \n")

        if conda_path:
            f.write("module load anaconda3 \n")
            f.write(f"source activate {conda_path} \n")

        f.write(
            'value=$(sed -n "${}p" {}) \n'.format("{SLURM_ARRAY_TASK_ID}", array_txt)
        )
        f.write("$value \n")
