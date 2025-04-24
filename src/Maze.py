from Cell import Cell
from Point import Point
import time
import random

class Maze:
  def __init__(
    self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win = None,
    seed = None,
  ):
    self._pos = Point(x1, y1)
    self.n_rows = num_rows
    self.n_cols = num_cols
    self.cell_width = cell_size_x
    self.cell_height = cell_size_y
    self._win = win
    self._cells = []
    self._create_cells()
    self._break_entrance_and_exit()
    if seed is not None:
      random.seed(seed)
    self._break_wall_r(0, 0)
    self._reset_cells_visited()

  def _reset_cells_visited(self):
    for row in self._cells:
      for cell in row:
        cell.visited = False

  def _create_cells(self):
    self._cells = [
      [
        Cell(
          Point(self._pos.x + col * self.cell_width, self._pos.y + row * self.cell_height),
          Point(self._pos.x + (col + 1) * self.cell_width, self._pos.y + (row + 1) * self.cell_height), 
          self._win
        ) for col in range(self.n_cols)
      ] for row in range(self.n_rows)
    ]
    if self._win is not None:
      for i in range(self.n_rows):
        for j in range(self.n_cols):
          self._cells[i][j].draw()
  
  def _draw_cell(self, i, j):
    self._cells[i][j].draw()
    self._animate()

  def _animate(self):
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._cells[self.n_rows - 1][self.n_cols - 1].has_bottom_wall = False
    if self._win is not None:
      self._draw_cell(0, 0)
      self._draw_cell(self.n_rows - 1, self.n_cols - 1)
      self._animate() 

  def _break_wall_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      possible_moves = []
      if i > 0 and not self._cells[i - 1][j].visited:
        possible_moves.append((i - 1, j))
      if i < self.n_rows - 1 and not self._cells[i + 1][j].visited:
        possible_moves.append((i + 1, j))
      if j > 0 and not self._cells[i][j - 1].visited:
        possible_moves.append((i, j - 1))
      if j < self.n_cols - 1 and not self._cells[i][j + 1].visited:
        possible_moves.append((i, j + 1))

      if not possible_moves:
        return
      
      next_cell = random.choice(possible_moves)
      ni, nj = next_cell
      if ni == i - 1:
        self._cells[i][j].has_top_wall = False
        self._cells[ni][nj].has_bottom_wall = False
      elif ni == i + 1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[ni][nj].has_top_wall = False
      elif nj == j - 1:
        self._cells[i][j].has_left_wall = False
        self._cells[ni][nj].has_right_wall = False
      elif nj == j + 1:
        self._cells[i][j].has_right_wall = False
        self._cells[ni][nj].has_left_wall = False

      if self._win is not None:
        self._draw_cell(i, j)
        self._draw_cell(ni, nj)
      self._break_wall_r(ni, nj)

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True
    if i == self.n_rows - 1 and j == self.n_cols - 1:
      return True
    if j < self.n_cols - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_right_wall:
      self._cells[i][j].draw_move(self._cells[i][j + 1])
      if self._solve_r(i, j + 1):
        return True
      self._cells[i][j].draw_move(self._cells[i][j + 1], True)
    if i < self.n_rows - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_bottom_wall:
      self._cells[i][j].draw_move(self._cells[i + 1][j])
      if self._solve_r(i + 1, j):
        return True
      self._cells[i][j].draw_move(self._cells[i + 1][j], True)
    if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_left_wall:
      self._cells[i][j].draw_move(self._cells[i][j - 1])
      if self._solve_r(i, j - 1):
        return True
      self._cells[i][j].draw_move(self._cells[i][j - 1], True)
    if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_top_wall:
      self._cells[i][j].draw_move(self._cells[i - 1][j])
      if self._solve_r(i - 1, j):
        return True
      self._cells[i][j].draw_move(self._cells[i - 1][j], True)
    return False
