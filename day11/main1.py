import math
from .parse import parse

def count_stones(stones, iterations):
  if iterations == 0:
    return len(stones)
  
  count = 0
  for stone in stones:
    if stone == 0:
      count += count_stones([1], iterations - 1)
    elif not ((math.floor(math.log10(stone)) + 1) % 2):
      str_stone = str(stone)
      half_length = len(str_stone) // 2
      new_stones = [int(str_stone[:half_length]), int(str_stone[half_length:])]
      count += count_stones(new_stones, iterations - 1)
    else:
      count += count_stones([stone * 2024], iterations - 1)
  return count

def main1():
  stones = parse("input.txt")
  print(count_stones(stones, 25))

if __name__ == "__main__":
  main1()