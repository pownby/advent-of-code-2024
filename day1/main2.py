from parse import parse

def main2():
  first, second = parse()

  second_counts = {}

  for n in second:
    second_counts[n] = second_counts[n] + 1 if n in second_counts else 1

  first_occurences = [int(n) * second_counts.get(n, 0) for n in first]

  print(sum(first_occurences))

if __name__ == "__main__":
  main2()