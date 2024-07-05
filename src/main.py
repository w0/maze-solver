from graphics import Window
from maze import Maze

from random import randrange

def main():
    
    win = Window(800,600)

    num_cols = 20
    num_rows = 30
    m1 = Maze(30, 30, num_rows, num_cols, 15, 15, win)
    m1.solve()

    win.wait_for_close()

main()