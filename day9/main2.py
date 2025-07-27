from .parse2 import parse

def main2():
  files, empties = parse("input.txt")
  for i in range(len(files) - 1, -1, -1):
    file = files[i]
    size = file.size
    # get first occurence of each size of empty block that will fit this file
    candidates = [empties[key][0] for key in empties if key >= size and len(empties[key])]
    # filter out anything not to the left of this file
    candidates = [c for c in candidates if c.start_index < file.start_index]
    if candidates:
      # get earliest-occuring candidate and merge file
      candidate = min(candidates, key=lambda x: x.start_index)
      candidate.merge_file(file, empties)

  print(sum([file.get_checksum() for file in files]))

if __name__ == "__main__":
  main2()