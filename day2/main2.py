from parse import parse

def report_is_safe(report, repeat = True):
  # will just cover increment case
  prev = report[0]
  for level in report[1:]:
    delta = level - prev
    if (delta < 1 or delta > 3):
      if (repeat):
        length = len(report)
        return any(report_is_safe(report[:i] + report[i + 1:], False) for i in range(length))
      return False
    prev = level
  return True



def main2():
  reports = parse("input.txt")
  safe_reports = [report for report in reports if report_is_safe(report) or report_is_safe(list(reversed(report)))]
  print(len(safe_reports))

if __name__ == "__main__":
  main2()