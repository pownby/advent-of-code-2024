from .parse import parse

DIRECTIONS = [
  [-1, -1], # up left
  [-1, 1], # up right
  [1, -1],
  [1, 1],
  [0, -1], # left
  [0, 1], # right
  [-1, 0],
  [1, 0]
]

NEXT_LETTER = {
  'X': 'M',
  'M': 'A',
  'A': 'S'
}

def isValid(row, col, grid):
  rowCount = len(grid)
  colCount = len(grid[0])
  return (row > -1 and row < rowCount and col > -1 and col < colCount)

def traverseDirection(row, col, grid, direction, match):
    if not isValid(row, col, grid):
      return 0
    
    letter = grid[row][col]
    nextLetter = NEXT_LETTER.get(letter)

    if letter == match:
      if (letter == 'S'):
        return 1
      else:
        [rowOffset, colOffset] = direction
        return traverseDirection(row + rowOffset, col + colOffset, grid, direction, nextLetter)
    else:
      return 0

def countWords(row, col, grid):
  count = 0

  for dir in DIRECTIONS:
      [rowOffset, colOffset] = dir
      count += traverseDirection(row + rowOffset, col + colOffset, grid, dir, 'M')

  return count


def main1():
  grid = parse("input.txt")
  rowCount = len(grid)
  colCount = len(grid[0])

  count = 0
  for row in range(rowCount):
    for col in range(colCount):
      if grid[row][col] == 'X':
        count += countWords(row, col, grid)
    
  print(count)

if __name__ == "__main__":
  main1()