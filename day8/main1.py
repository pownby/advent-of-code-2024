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

def is_valid(row, col, row_count, col_count):
  return (row > -1 and row < row_count and col > -1 and col < col_count)

def get_antinodes_dimension(a, b):
  delta = a - b
  x = a + delta
  y = b - delta
  return x, y

def get_antinodes(a, b, row_count, col_count):
  [a_row, a_col] = a
  [b_row, b_col] = b
  x_row, y_row = get_antinodes_dimension(a_row, b_row)
  x_col, y_col = get_antinodes_dimension(a_col, b_col)

  antinodes = []
  if is_valid(x_row, x_col, row_count, col_count):
    antinodes.append([x_row, x_col])
  if is_valid(y_row, y_col, row_count, col_count):
    antinodes.append([y_row, y_col])
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

def main1():
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
  main1()