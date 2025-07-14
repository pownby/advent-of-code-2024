from .parse import parse

def can_evaluate_value(value, operands, running_total = 0):
  if running_total > value:
    return False
  operand = operands[0]
  concat_result = int(str(running_total) + str(operand))
  mult_result = (running_total or 1) * operand
  add_result = running_total + operand

  if len(operands) == 1:
    return ((concat_result == value) or
            (mult_result == value) or
            (add_result == value))
  
  remaining_operands = operands[1:]
  
  return (can_evaluate_value(value, remaining_operands, concat_result) or
          can_evaluate_value(value, remaining_operands, mult_result) or
          can_evaluate_value(value, remaining_operands, add_result))

def main2():
  equations = parse("input.txt")

  sum = 0
  for [value, operands] in equations:
    if can_evaluate_value(value, operands):
      sum += value
  
  print(sum)

if __name__ == "__main__":
  main2()