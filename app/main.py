from utils import *
from data import grid

def check_move(grid, row, column, value):
  if grid[row][column] != 0:
    print("\n[ERROR] You cannot modify a cell that is already filled!")
  elif is_valid_move(grid, row, column, value):
    grid[row][column] = value
  else:
    print("\n[ERROR] Move not valid, try again!\n")

def run_sodoku_game():
  is_continue = True

  while is_continue:
    print_grid(grid)

    if check_win(grid):
      print("Congratulations! You resolved the Sodoku!")
      is_continue = False

    move = input("\nInsert the move (row column value): ")

    try:
      row, column, value = map(int, move.split())
      check_move(grid, row - 1, column - 1, value)
    except ValueError:
      print("\n[ERROR] Input not valid. Use the format: row column number (e.g. 1 3 4)")

run_sodoku_game()
