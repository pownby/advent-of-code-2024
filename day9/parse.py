import os
from common_utils.readFileLines import readFileLines

CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
  line = readFileLines(f"{CURRENT_DIR}/{file_name}")[0]
  disk = []
  id = 0
  
  for line_index in range(0, len(line), 2):
    file_size = int(line[line_index])
    for i in range(file_size):
      disk.append(id)
    if line_index + 1 < len(line):
      empty_size = int(line[line_index + 1])
      for j in range(empty_size):
        disk.append(None)
    id += 1
  return disk
    

# Example usage
if __name__ == "__main__":
  data_sets = parse(DEFAULT_FILE)
  print(data_sets)