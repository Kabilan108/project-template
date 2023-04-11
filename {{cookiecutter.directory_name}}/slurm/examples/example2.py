import argparse
import yaml

# Parse the yaml file argument
parser = argparse.ArgumentParser()
parser.add_argument("--yaml_file", type=str, help="yaml file with arguments")
args = parser.parse_args()

# Load the yaml file
with open(args.yaml_file, "r") as f:
    data = yaml.safe_load(f)

# Print the arguments from the yaml file
print(f"Hello, my name is {data['name']}.")
print(f"I am {data['age']} years old.")
print(f"My hobby is {data['hobby']}.")