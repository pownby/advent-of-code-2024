import math
from .parse import parse

def blink(stones):
  i = 0
  while i < len(stones):
    stone = stones[i]
    if stone == 0:
      stones[i] = 1
    # elif not (len(str(stone)) % 2):
    elif not ((math.floor(math.log10(stone)) + 1) % 2):
      str_stone = str(stone)
      half_length = len(str(stone)) // 2
      new_stones = [int(str_stone[:half_length]), int(str_stone[half_length:])]
      stones = stones[:i] + new_stones + stones[i+1:]
      i += 1
    else:
      stones[i] = stone * 2024
    i += 1
  return stones

def naive():
  stones = parse("input.txt")

  for i in range(25):
    stones = blink(stones)

  print(len(stones))

if __name__ == "__main__":
  naive()