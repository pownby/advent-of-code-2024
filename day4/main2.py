from .parse import parse

DIAGONALS = [
  [
    [-1, -1], # up left
    [1, 1]
  ],
  [
    [1, -1],
    [-1, 1] # up right
  ]
]

def isValidA(row, col, grid):
  # is valid A of MAS
  rowCount = len(grid)
  colCount = len(grid[0])
  return (row > 0 and row < rowCount - 1 and col > 0 and col < colCount - 1)
    
def isMas(row, col, grid, diagonal):
  [offset1, offset2] = diagonal
  [row_offset1, col_offset1] = offset1
  [row_offset2, col_offset2] = offset2
  letter1 = grid[row + row_offset1][col + col_offset1]
  letter2 = grid[row + row_offset2][col + col_offset2]
  return (letter1 == 'M' and letter2 == 'S') or (letter1 == 'S' and letter2 == 'M')

def isXmas(row, col, grid):
  if isValidA(row, col, grid):
    return all([isMas(row, col, grid, diagonal) for diagonal in DIAGONALS])
  return False

# we'll find each A and see if there are two MAS in the diagnonals
def main2():
  grid = parse("input.txt")
  rowCount = len(grid)
  colCount = len(grid[0])

  count = 0
  for row in range(rowCount):
    for col in range(colCount):
      if grid[row][col] == 'A':
        count = count + (1 if isXmas(row, col, grid) else 0)
    
  print(count)

if __name__ == "__main__":
  main2()