from graphics import Window, Point, Line, Cell

from random import randrange

def main():
    
    win = Window(800,600)

    p2 = Point(400, 500)
    p1 = Point(500, 400)
    
    my_cell = Cell(p1, p2, win)
    my_cell.draw()

    win.wait_for_close()

main()