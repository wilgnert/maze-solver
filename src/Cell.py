from Line import Line
from Point import Point

class Cell:
  def __init__(self, a: Point, b: Point):
    self.__a = a
    self.__b = b
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    
  def draw(self, canvas):
    top_left = self.__a
    top_right = Point(self.__b.x, self.__a.y)
    bottom_left = Point(self.__a.x, self.__b.y)
    bottom_right = self.__b
    if self.has_top_wall:
      Line(top_left, top_right).draw(canvas, "black")
    if self.has_left_wall:
      Line(top_left, bottom_left).draw(canvas, "black")
    if self.has_right_wall:
      Line(top_right, bottom_right).draw(canvas, "black")
    if self.has_bottom_wall:
      Line(bottom_left, bottom_right).draw(canvas, "black")