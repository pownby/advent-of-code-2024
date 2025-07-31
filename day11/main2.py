import math
import json
import os
from .parse import parse
from .read_pre_computed import read_pre_computed

CURRENT_DIR = os.path.dirname(__file__)

def get_single_digit_count(digit, next_stone, iterations, computed):
  if iterations in computed[digit]:
    return computed[digit][iterations]
  else:
    computed_count = count_stones(next_stone, iterations - 1, computed)
    computed[digit][iterations] = computed_count
    return computed_count

def count_stones(stone, iterations, computed):
  if iterations == 0:
    return 1
  
  if stone in computed and iterations in computed[stone]:
    return computed[stone][iterations]
  
  if stone == 0:
    computed_count = count_stones(1, iterations - 1, computed)
    computed[0][iterations] = computed_count
    return computed_count
  
  if not ((math.floor(math.log10(stone)) + 1) % 2):
    str_stone = str(stone)
    half_length = len(str_stone) // 2
    first_half = int(str_stone[:half_length])
    second_half = int(str_stone[half_length:])
    return (
      count_stones(first_half, iterations - 1, computed)
    ) + (
      count_stones(second_half, iterations - 1, computed)
    )
  return count_stones(stone * 2024, iterations - 1, computed)

def pre_compute(digit_range, iterations, pre_computed):
  for digit in digit_range:
    if digit not in pre_computed:
      pre_computed[digit] = {}

    last_computed = len(pre_computed[digit]) - 1
    if last_computed < iterations:
      for i in range(last_computed + 1, iterations + 1):
        pre_computed[digit][i] = count_stones(digit, i, pre_computed)
  
  with open(f"{CURRENT_DIR}/pre-computed.json", "w") as file:
    json.dump(pre_computed, file, indent=2)

ITERATIONS = 75

def display_partial(stones, computed):
  count = 0
  for i, stone in enumerate(stones):
    stone_count = count_stones(stone, ITERATIONS, computed)
    print(f"({i}) {stone}: {stone_count}")
    count += stone_count
  print(f"total {count}")

def main2():
  stones = parse("input.txt")
  pre_computed = read_pre_computed()
  display_partial(stones, pre_computed)
  # pre_compute(range(10), 75, pre_computed)

if __name__ == "__main__":
  main2()