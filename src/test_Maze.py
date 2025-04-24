import unittest
from Maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(
        len(m1._cells),
        num_rows,
    )
    self.assertEqual(
        len(m1._cells[0]),
        num_cols,
    )

  def test_maze_create_cells_different_sizes(self):
    # Test with a larger maze
    num_cols = 20
    num_rows = 15
    m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(len(m2._cells), num_rows)
    self.assertEqual(len(m2._cells[0]), num_cols)

    # Test with a smaller maze
    num_cols = 5
    num_rows = 3
    m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(len(m3._cells), num_rows)
    self.assertEqual(len(m3._cells[0]), num_cols)

  def test_maze_entrance_and_exit(self):
    num_cols = 10
    num_rows = 10
    m = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertFalse(m._cells[0][0].has_top_wall)
    self.assertFalse(m._cells[num_rows - 1][num_cols - 1].has_bottom_wall)

  def test_maze_reset_cells_visited(self):
    num_cols = 5
    num_rows = 5
    m = Maze(0, 0, num_rows, num_cols, 10, 10)
    for row in m._cells:
        for cell in row:
            self.assertFalse(cell.visited)

  def test_maze_random_seed(self):
    num_cols = 5
    num_rows = 5
    seed = 42
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=seed)
    m2 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=seed)
    self.assertEqual(
            [[cell.visited for cell in row] for row in m1._cells],
            [[cell.visited for cell in row] for row in m2._cells],
    )

if __name__ == "__main__":
    unittest.main()