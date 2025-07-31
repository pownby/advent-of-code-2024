import json
import os

CURRENT_DIR = os.path.dirname(__file__)

def read_pre_computed():
  with open(f"{CURRENT_DIR}/pre-computed.json", "r") as file:
      data = json.load(file)
      # convert strings keys to ints
      converted = {}
      for str_digit in data:
         int_digit = int(str_digit)
         converted[int_digit] = {}
         for str_iterations in data[str_digit]:
            int_iterations = int(str_iterations)
            converted[int_digit][int_iterations] = data[str_digit][str_iterations]

      return converted
      