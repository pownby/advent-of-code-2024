from parse import parse

def main1():
  first, second = parse()
  first.sort()
  second.sort()
  
  sum = 0
  for i in range(len(first)):
    sum = sum + abs(int(first[i]) - int(second[i]))

  print(sum)

if __name__ == "__main__":
  main1()