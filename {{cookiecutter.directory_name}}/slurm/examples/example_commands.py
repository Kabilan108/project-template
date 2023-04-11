import os
import sys
from commands import generic_yaml_command
from sbatch import submit_array

# Get the arguments from the command line
root_dir = sys.argv[1]
node_setting = " ".join(sys.argv[2:-2])
job_name = sys.argv[-2]
conda_path = sys.argv[-1]

# Define the path to the example.py script
py_path = os.path.join(root_dir, "example.py")

# Define a list of yaml files with different arguments
yaml_files = [
    os.path.join(root_dir, "example.yaml"),
    os.path.join(root_dir, "example2.yaml"),
    os.path.join(root_dir, "example3.yaml"),
]

# Generate a list of commands using the generic_yaml_command function
command_list = []
for yaml_file in yaml_files:
    command = generic_yaml_command(py_path, yaml_file)
    command_list.append(command)

# Submit the job array using the submit_array function
submit_array(root_dir, command_list, node_setting, job_name, conda_path)