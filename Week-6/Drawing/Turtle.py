import math

class Turtle:
    def __init__(self, pen, start_x=0, start_y=0, start_angle=0, step=50, turn_angle=90):
        self.pen = pen
        self.x = start_x
        self.y = start_y
        self.angle = start_angle
        self.step = step
        self.turn_angle = turn_angle
        self.pen.move_to(self.x, self.y)  # Set initial position

    def move_forward(self, distance):
        rad = math.radians(self.angle)
        new_x = self.x + self.step * math.cos(rad)
        new_y = self.y + self.step * math.sin(rad)
        self.pen.line_to(new_x, new_y)
        self.x, self.y = new_x, new_y

    def turn_right(self, distance):
        self.angle = (self.angle + self.turn_angle) % 360

    def turn_left(self, distance):
        self.angle =  (self.angle - self.turn_angle) % 360