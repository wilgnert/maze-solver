from Window import Window
from Point import Point
from Line import Line
from Cell import Cell

CELL_SIZE = 100
PADDING = 100
WIDTH = 800
HEIGHT = 800

def main():
  win = Window(WIDTH, HEIGHT)
  cells = [Cell(
    Point(PADDING + col * CELL_SIZE, PADDING + row * CELL_SIZE),
    Point(PADDING + (col + 1) * CELL_SIZE, PADDING + (row + 1) * CELL_SIZE),
  ) for col in range(int((WIDTH - 2 * PADDING) / CELL_SIZE)) for row in range(int((HEIGHT - 2 * PADDING) / CELL_SIZE))]
  for cell in cells: 
    win.draw_cell(cell)
  win.wait_for_close()

if __name__ == "__main__":
  main()