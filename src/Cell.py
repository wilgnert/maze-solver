from Line import Line
from Point import Point

class Cell:
  def __init__(self, a: Point, b: Point, win):
    self.__a = a
    self.__b = b
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._win = win
    self.visited = False
    
  def draw(self):
    canvas = self._win.getCanvas()
    top_left = self.__a
    top_right = Point(self.__b.x, self.__a.y)
    bottom_left = Point(self.__a.x, self.__b.y)
    bottom_right = self.__b
    Line(top_left, top_right).draw(canvas, "#d9d9d9")
    Line(top_left, bottom_left).draw(canvas, "#d9d9d9")
    Line(top_right, bottom_right).draw(canvas, "#d9d9d9")
    Line(bottom_left, bottom_right).draw(canvas, "#d9d9d9")

    if self.has_top_wall:
      Line(top_left, top_right).draw(canvas, "black")
    if self.has_left_wall:
      Line(top_left, bottom_left).draw(canvas, "black")
    if self.has_right_wall:
      Line(top_right, bottom_right).draw(canvas, "black")
    if self.has_bottom_wall:
      Line(bottom_left, bottom_right).draw(canvas, "black")

  def getMidPoint(self) -> Point:
    return Point((self.__a.x + self.__b.x) // 2, (self.__a.y + self.__b.y) // 2)

  def draw_move(self, other: "Cell", undo = False):
    m1, m2 = self.getMidPoint(), other.getMidPoint()
    Line(m1, m2).draw(self._win.getCanvas(), "gray" if undo else "red")