import os
from common_utils.readFileLines import readFileLines
from .entity import File, Empty
  
CURRENT_DIR = os.path.dirname(__file__)
DEFAULT_FILE = "input.txt"

def parse(file_name = DEFAULT_FILE):
  line = readFileLines(f"{CURRENT_DIR}/{file_name}")[0]
  files = []
  empties = {}
  disk_index = 0
  
  for line_index in range(0, len(line), 2):
    file_size = int(line[line_index])
    if file_size:
      files.append(File(disk_index, file_size))
    disk_index += file_size
    if line_index + 1 < len(line):
      empty_size = int(line[line_index + 1])
      if empty_size:
        new_empty = Empty(disk_index, empty_size)
        new_empty.add_to_empties(empties, True)
      disk_index += empty_size

  return files, empties

# Example usage
if __name__ == "__main__":
  files, empties = parse(DEFAULT_FILE)
  print(files, empties)