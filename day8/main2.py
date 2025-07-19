from .parse import parse

def build_antenna_map(grid):
  antennas = {}

  for row_i, row in enumerate(grid):
    for col_i, cell in enumerate(row):
      if cell != '.':
        antennas_group = antennas.get(cell) or []
        antennas_group.append([row_i, col_i])
        antennas[cell] = antennas_group
  return antennas

def is_valid(node, row_count, col_count):
  [row, col] = node
  return (row > -1 and row < row_count and col > -1 and col < col_count)

def get_antinode_factories(a, b):
  [a_row, a_col] = a
  [b_row, b_col] = b
  delta_row = a_row - b_row
  delta_col = a_col - b_col

  def get_next_x(x):
    [x_row, x_col] = x
    return [x_row + delta_row, x_col + delta_col]
  
  def get_next_y(y):
    [y_row, y_col] = y
    return [y_row - delta_row, y_col - delta_col]
  
  return get_next_x, get_next_y

def get_antinodes(a, b, row_count, col_count):
  antinodes = [a, b]
  get_next_x, get_next_y = get_antinode_factories(a, b)
  x = get_next_x(a)
  y = get_next_y(b)

  while is_valid(x, row_count, col_count):
    antinodes.append(x)
    x = get_next_x(x)
  while is_valid(y, row_count, col_count):
    antinodes.append(y)
    y = get_next_y(y)
  return antinodes

def do_for_all_pairs(li, fn):
  for i in range(len(li)):
    for j in li[i + 1:]:
      fn(li[i], j)

def visualize(grid, antinodes):
  row_count = len(grid)
  col_count = len(grid[0])

  for row in range(row_count):
    row_str = ""
    for col in range(col_count):
      if grid[row][col] != '.':
        row_str += grid[row][col]
      elif antinodes[row][col]:
        row_str += '#'
      else:
        row_str += '.'
    print(row_str)

def main2():
  grid = parse("input.txt")
  row_count = len(grid)
  col_count = len(grid[0])

  antinodes = [[False for i in range(col_count)] for j in range(row_count)]
  antennas = build_antenna_map(grid)

  def set_antinodes(a, b):
    for [anti_row, anti_col] in get_antinodes(a, b, row_count, col_count):
      antinodes[anti_row][anti_col] = True

  for antenna_list in antennas.values():
    do_for_all_pairs(antenna_list, set_antinodes)

  print(sum([len([v_col for v_col in v_row if v_col]) for v_row in antinodes]))
  # visualize(grid, antinodes)

if __name__ == "__main__":
  main2()