from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"

        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__p1 = point1
        self.__p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__p1.x,
            self.__p1.y,
            self.__p2.x,
            self.__p2.y,
            fill=fill_color,
            width=2
        )
    
class Cell:
    def __init__(self, point1: Point, point2: Point, window: Window):
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True

        self.__x1 = point1.x
        self.__y1 = point1.y

        self.__x2 = point2.x
        self.__y2 = point2.y

        self.__win = window

    def draw(self):
        b_left = Point(self.__x1, self.__y2)
        b_right = Point(self.__x2, self.__y2)
        t_left = Point(self.__x1, self.__y1)
        t_right = Point(self.__x2, self.__y1)

        if self.has_bottom_wall:
            self.__win.draw_line(Line(b_left, b_right), "red")

        if self.has_left_wall:
            self.__win.draw_line(Line(b_left, t_left), "red")
        
        if self.has_top_wall:
            self.__win.draw_line(Line(t_left, t_right), "blue")
        
        if self.has_right_wall:
            self.__win.draw_line(Line(t_right, b_right), "blue")
