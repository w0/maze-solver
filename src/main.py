from graphics import Window, Point, Line

from random import randrange

def main():
    
    win = Window(800,600)

    count = 0
    p_sets = 15

    while count < p_sets:
        p1 = Point(randrange(800), randrange(600))
        p2 = Point(randrange(800), randrange(600))
        win.draw_line(Line(p1, p2), "black")
        count += 1
    
    win.wait_for_close()

main()