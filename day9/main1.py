from .parse import parse

def main1():
  disk = parse("input.txt")
  
  def fragment():
    current = len(disk) - 1
    while current > -1:
      if disk[current] is not None:
        yield current
      current -= 1

  checksum = 0

  for index, block in enumerate(disk):
    if block is not None:
      checksum += index * block
    else:
      next_fragment = next(fragment())
      if next_fragment <= index:
        break
      checksum += index * disk[next_fragment]
      disk[index] = disk[next_fragment] # unnecessary, but useful for visualization
      disk[next_fragment] = None

  print(checksum)
  

if __name__ == "__main__":
  main1()