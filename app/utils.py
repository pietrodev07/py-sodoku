def print_grid(grid):
  print()

  for row in grid:
    print("  ".join(str(cell) if cell != 0 else "." for cell in row))

def is_valid_move(grid, row, column, value):
  if value in grid[row]:
    return False
  
  for i in range(9):
    if grid[i][column] == value:
      return False

  starting_row = (row // 3) * 3
  starting_column = (column // 3) * 3

  for i in range(starting_row, starting_row + 3):
    for j in range(starting_column, starting_column + 3):
      if grid[i][j] == value:
        return False
  
  return True

def check_win(grid):
  for i in range(9):
    for j in range(9):
      value = grid[i][j]
      if value == 0 or not is_valid_move(grid, i, j, value):
        return False

  return True
