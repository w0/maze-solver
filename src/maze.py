from cell import Cell
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
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)  

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while True:
            possible = []

            # Check up (j - 1)
            if j > 0 and not self._cells[i][j - 1].visited:
                possible.append([i, j - 1])

            # Check down (j + 1)
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible.append([i, j + 1])

            # Check left (i - 1)
            if i > 0 and not self._cells[i - 1][j].visited:
                possible.append([i - 1, j])

            # Check right (i + 1)
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible.append([i + 1, j])

            # List is empty
            if not possible:
                self._draw_cell(i, j)
                break
            
            random_direction = random.randrange(len(possible))
            next_cell = possible[random_direction]


            # Up
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            
            # Down
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            # Left
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            
            # Right
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])


    def _reset_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # Check up 
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_cell(self._cells[i][j-1])
            # Move 
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_cell(self._cells[i][j-1], True)
        
        # Check down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_cell(self._cells[i][j+1])
            # Move 
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_cell(self._cells[i][j+1], True)

        # Check left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_cell(self._cells[i-1][j])
            # Move 
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_cell(self._cells[i-1][j], True)
        
        # Check right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_cell(self._cells[i+1][j])
            # Move 
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_cell(self._cells[i+1][j], True)

        return False