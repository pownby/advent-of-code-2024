import re
from .parse import parse

RE_INSTRUCTIONS = re.compile(r'mul\(\d+,\d+\)')
RE_NUMBERS = re.compile(r'\d+')

def main1():
  memory = parse("input.txt")

  sum = 0
  for line in memory:
    matches = re.findall(RE_INSTRUCTIONS, line)

    for match in matches:
      numbers = re.findall(RE_NUMBERS, match)
      sum += int(numbers[0]) * int(numbers[1])
    
  print(sum)

if __name__ == "__main__":
  main1()