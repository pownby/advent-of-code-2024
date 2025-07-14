import os
from common_utils.readFileLines import readFileLines

CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
  lines = readFileLines(f"{CURRENT_DIR}/{file_name}")
  
  equations = []
  for line in lines:
    line_parts = line.split(':')
    value = int(line_parts[0])
    operands = [int(operand) for operand in line_parts[1].strip().split(' ')]
    equations.append([
      value,
      operands
    ])

  return equations

# Example usage
if __name__ == "__main__":
  data_sets = parse(DEFAULT_FILE)
  print(data_sets)