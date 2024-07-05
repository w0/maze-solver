from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title = "Maze Solver"

        self._canvas = Canvas(self._root, width=width, height=height, background="#323232")
        self._canvas.pack()
        
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True

        while self._running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self._p1 = point1
        self._p2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self._p1.x,
            self._p1.y,
            self._p2.x,
            self._p2.y,
            fill=fill_color,
            width=2
        )
    
