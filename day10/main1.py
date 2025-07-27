from .parse import parse

ROW_OFFSETS = [-1, 0, 1, 0]
COL_OFFSETS = [0, 1, 0, -1]

def get_dimensions(grid):
  row_count = len(grid)
  col_count = len(grid[0])
  return row_count, col_count

def is_valid(row, col, grid):
  row_count, col_count = get_dimensions(grid)
  return (row > -1 and row < row_count and col > -1 and col < col_count)

def get_peaks(row, col, grid, height, found_peaks):
  if (height == 9):
    found_peaks.add((row, col))
  else:  
    for i in range(4):
      next_row = row + ROW_OFFSETS[i]
      next_col = col + COL_OFFSETS[i]
      if (is_valid(next_row, next_col, grid)):
        next_height = grid[next_row][next_col]
        if (next_height == height + 1):
          get_peaks(next_row, next_col, grid, next_height, found_peaks)
  return found_peaks

def main1():
  grid = parse("input.txt")
  row_count, col_count = get_dimensions(grid)

  total_score = 0
  for row in range(row_count):
    for col in range(col_count):
      if grid[row][col] == 0:
        peaks = get_peaks(row, col, grid, 0, set({}))
        total_score += len(peaks)

  print(total_score)

if __name__ == "__main__":
  main1()