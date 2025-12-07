from Geometry.Point import Point

class Pen:

    #Initialize pen on a drawing canvas at origin (0,0)
    def __init__(self, canvas):
        self._canvas = canvas
        self._cp = Point(0, 0)   #Stores current position(Point(x,y)) of Pen

    #Simply moves position of pen
    def move_to(self, x, y):
        self._cp = Point(x, y)         #Moves pen to new position without drawing anything.

    #Simply draws a line from 'cp' to 'new_point'
    def line_to(self, x, y):
        new_point = Point(x, y)
        self._canvas.add_line(self._cp, new_point)
        self._cp = new_point           #Assigns the new position(Point(x1,y1)) of pen to current position

    @property
    def get_position(self):
        return self._cp
