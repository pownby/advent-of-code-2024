import os
from common_utils.readFileLines import readFileLines

CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
    lines = readFileLines(f"{CURRENT_DIR}/{file_name}")
    return [[int(n) for n in line.split(' ')] for line in lines]

# Example usage
if __name__ == "__main__":
    data_sets = parse(DEFAULT_FILE)
    print(data_sets)