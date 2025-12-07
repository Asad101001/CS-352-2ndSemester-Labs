from Drawing.Command import MoveForwardCommand
from Drawing.Command import TurnRightCommand
from Drawing.Command import TurnLeftCommand

class InputModule:
    def __init__(self, step=50, turn_angle=90):
        self.step = step
        self.turn_angle = turn_angle
        self.command_map = {
            'F': lambda: MoveForwardCommand(self.step),
            '+': lambda: TurnRightCommand(self.turn_angle),
            '-': lambda: TurnLeftCommand(self.turn_angle)
        }

    def parse(self, command_string):
        commands = []
        tokens = command_string.strip().split()  # space-separated
        for token in tokens:
            if token in self.command_map:
                commands.append(self.command_map[token]())
        return commands
