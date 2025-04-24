from Window import Window
from Point import Point
from Line import Line
from Cell import Cell
from Maze import Maze

CELL_SIZE = 20
PADDING = 20
WIDTH = 800
HEIGHT = 600

def main():
  win = Window(WIDTH, HEIGHT)
  maze = Maze(
    PADDING,
    PADDING,
    (HEIGHT - 2 * PADDING) // CELL_SIZE,
    (WIDTH - 2 * PADDING) // CELL_SIZE,
    CELL_SIZE,
    CELL_SIZE,
    win
  )
  maze.solve()
  win.wait_for_close()

if __name__ == "__main__":
  main()