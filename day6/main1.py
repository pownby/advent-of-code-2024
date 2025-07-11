from enum import Enum
from .parse import parse

class DirectionType(Enum):
  UP = "UP"
  RIGHT = "RIGHT"
  DOWN = "DOWN"
  LEFT = "LEFT"

DIRECTION_OFFSETS = {
  DirectionType.LEFT: [0, -1], 
  DirectionType.RIGHT: [0, 1],
  DirectionType.UP: [-1, 0],
  DirectionType.DOWN: [1, 0]
}

NEXT_DIRECTION = {
  DirectionType.UP: DirectionType.RIGHT,
  DirectionType.RIGHT: DirectionType.DOWN,
  DirectionType.DOWN: DirectionType.LEFT,
  DirectionType.LEFT: DirectionType.UP
}

def is_valid(row, col, grid):
  rowCount = len(grid)
  colCount = len(grid[0])
  return (row > -1 and row < rowCount and col > -1 and col < colCount)

def get_start_pos(grid):
  rowCount = len(grid)
  colCount = len(grid[0])

  for row in range(rowCount):
    for col in range(colCount):
      if grid[row][col] == '^':
        return row, col
      
def get_next_pos(row, col, dir):
  [rowOffset, colOffset] = DIRECTION_OFFSETS[dir]
  return row + rowOffset, col + colOffset

def main1():
  grid = parse("input.txt")
  rowCount = len(grid)
  colCount = len(grid[0])

  visited = [[False for i in range(colCount)] for j in range(rowCount)]

  row, col = get_start_pos(grid)
  dir = DirectionType.UP
  visited[row][col] = True
  next_row, next_col = get_next_pos(row, col, dir)

  while is_valid(next_row, next_col, grid):
    if grid[next_row][next_col] != '#':
      row, col = next_row, next_col
      visited[row][col] = True
    else:
      dir = NEXT_DIRECTION[dir]
    next_row, next_col = get_next_pos(row, col, dir)

  print(sum([len([v_col for v_col in v_row if v_col]) for v_row in visited]))

if __name__ == "__main__":
  main1()