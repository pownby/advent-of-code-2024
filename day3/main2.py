import re
from .parse import parse

RE_INSTRUCTIONS = re.compile(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)')
RE_NUMBERS = re.compile(r'\d+')

def main2():
  memory = parse("input.txt")
  enable_instructions = True

  sum = 0
  for line in memory:
    matches = re.findall(RE_INSTRUCTIONS, line)

    for match in matches:
      if match == "do()":
        enable_instructions = True
      elif match == "don't()":
        enable_instructions = False
      elif enable_instructions:
        numbers = re.findall(RE_NUMBERS, match)
        sum += int(numbers[0]) * int(numbers[1])
    
  print(sum)

if __name__ == "__main__":
  main2()