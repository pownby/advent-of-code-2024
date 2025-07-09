from .parse import parse

def get_middle_num(order):
  return order[len(order) // 2]

def is_bad_order(order, ordering_dict):
  for i, page in enumerate(order):
    pages_required_after = ordering_dict.get(page) or set({})
    if any(preceding_page in pages_required_after for preceding_page in order[:i]):
      return True
  return False

def rearrange_order(order, from_index, to_index):
  new_order = list(order)
  page = new_order.pop(from_index)
  new_order.insert(to_index, page) # This may be a bug if to is after from, but we should always be before
  return new_order


def fix_order(order, ordering_dict):
  for i, page in enumerate(order):
    pages_required_after = ordering_dict.get(page) or set({})
    for j, preceding_page in enumerate(order[:i]):
      if preceding_page in pages_required_after:
        return fix_order(rearrange_order(order, i, j), ordering_dict)
  return order

def create_ordering_dict(ordering_rules):
  ordering_dict = {}
  for rule in ordering_rules:
    [key, page] = rule
    if key in ordering_dict:
      ordering_dict[key].add(page)
    else :
      ordering_dict[key] = set([page])
  return ordering_dict

def main2():
  ordering_rules, orders = parse("input.txt")
  ordering_dict = create_ordering_dict(ordering_rules)
  bad_orders = [order for order in orders if is_bad_order(order, ordering_dict)]

  print(sum(get_middle_num(fix_order(order, ordering_dict)) for order in bad_orders))

if __name__ == "__main__":
  main2()