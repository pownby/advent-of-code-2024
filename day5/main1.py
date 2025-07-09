from .parse import parse

def get_middle_num(order):
  return order[len(order) // 2]

def get_order_score(order, ordering_dict):
  for i, page in enumerate(order):
    # just try a naive, suboptimal approach and see how slow it is
    pages_required_after = ordering_dict.get(page) or set({})
    if any(preceding_page in pages_required_after for preceding_page in order[:i]):
      return 0
  return get_middle_num(order)

def create_ordering_dict(ordering_rules):
  ordering_dict = {}
  for rule in ordering_rules:
    [key, page] = rule
    if key in ordering_dict:
      ordering_dict[key].add(page)
    else :
      ordering_dict[key] = set([page])
  return ordering_dict

def main1():
  ordering_rules, orders = parse("input.txt")
  ordering_dict = create_ordering_dict(ordering_rules)

  print(sum(get_order_score(order, ordering_dict) for order in orders))

if __name__ == "__main__":
  main1()