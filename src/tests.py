import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_remove_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[12 - 1][10 - 1].has_right_wall,
            False
        )

    def test_cells_not_visited(self):
        num_cols = 5
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )



if __name__ == "__main__":
    unittest.main()