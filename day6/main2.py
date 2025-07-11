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

def get_moves_key(row, col, dir):
  return f"{row}:{col} {dir}"

def is_loop(start_row, start_col, grid):
  row, col = start_row, start_col
  dir = DirectionType.UP
  moves = set([get_moves_key(row, col, dir)])
  next_row, next_col = get_next_pos(row, col, dir)

  while is_valid(next_row, next_col, grid):
    next_move_key = get_moves_key(next_row, next_col, dir)
    if (next_move_key in moves):
      return True
    
    if grid[next_row][next_col] != '#':
      row, col = next_row, next_col
    else:
      dir = NEXT_DIRECTION[dir]
    next_row, next_col = get_next_pos(row, col, dir)
    moves.add(get_moves_key(row, col, dir))
  
  return False

def main2():
  grid = parse("input.txt")
  start_row, start_col = get_start_pos(grid)
  rowCount = len(grid)
  colCount = len(grid[0])

  sum = 0
  for row in range(rowCount):
    for col in range(colCount):
      if grid[row][col] == '.':
        grid[row][col] = '#'
        if is_loop(start_row, start_col, grid):
          sum += 1
        grid[row][col] = '.'

  print(sum)

if __name__ == "__main__":
  main2()