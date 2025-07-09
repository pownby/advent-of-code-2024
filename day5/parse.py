import os
from common_utils.readFileLines import readFileLines

CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
  lines = readFileLines(f"{CURRENT_DIR}/{file_name}")
  is_ordering_rules = True
  ordering_rules = []
  orders = []
  for line in lines:
    if not line:
      is_ordering_rules = False
    else:
      if is_ordering_rules:
        ordering_rules.append([int(n) for n in line.split("|")])
      else:
        orders.append([int(n) for n in line.split(",")])
  return ordering_rules, orders
        

# Example usage
if __name__ == "__main__":
  data_sets = parse(DEFAULT_FILE)
  print(data_sets)