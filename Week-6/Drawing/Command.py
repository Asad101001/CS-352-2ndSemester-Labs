class Command:
    def execute(self, turtle):
        raise NotImplementedError

class MoveForwardCommand(Command):
    def __init__(self, distance):
        self.distance = distance
    def execute(self, turtle):
        turtle.move_forward(self.distance)

class TurnRightCommand(Command):
    def __init__(self, degrees):
        self.degrees = degrees
    def execute(self, turtle):
        turtle.turn_right(self.degrees)

class TurnLeftCommand(Command):
    def __init__(self, degrees):
        self.degrees = degrees
    def execute(self, turtle):
        turtle.turn_left(self.degrees)
