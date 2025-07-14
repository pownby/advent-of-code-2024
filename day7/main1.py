from .parse import parse

def can_evaluate_value(value, operands, running_total = 0):
  if running_total > value:
    return False
  operand = operands[0]
  if len(operands) == 1:
    return (running_total + operand == value) or ((running_total or 1) * operand == value)
  
  remaining_operands = operands[1:]
  
  return (can_evaluate_value(value, remaining_operands, running_total + operand) or 
          can_evaluate_value(value, remaining_operands, (running_total or 1) * operand))

def main1():
  equations = parse("input.txt")

  sum = 0
  for [value, operands] in equations:
    if can_evaluate_value(value, operands):
      sum += value
  
  print(sum)

if __name__ == "__main__":
  main1()