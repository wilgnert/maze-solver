from Window import Window
from Point import Point
from Line import Line

def main():
  line1 = Line(Point(0, 0), Point(800, 600))
  line2 = Line(Point(800, 0), Point(0, 600))
  win = Window(800, 600)
  win.draw_line(line=line1, fill_color="black")
  win.draw_line(line=line2, fill_color="red")
  win.wait_for_close()

if __name__ == "__main__":
  main()