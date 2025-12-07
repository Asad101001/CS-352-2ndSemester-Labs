import tkinter as tk
from Drawing.Canvas import TKPanel
from Drawing.Pen import Pen
from Drawing.Turtle import Turtle
from Application.InputModule import InputModule

class App:
    def __init__(self, width=800, height=800):
        self.root = tk.Tk()
        self.root.title("Turtle Command Drawing")
        self.canvas = TKPanel(self.root, width=width, height=height)
        self.canvas.pack()

        self.pen = Pen(self.canvas)
        self.turtle = Turtle(self.pen, start_x=200, start_y=200)
        self.parser = InputModule(step=50, turn_angle=90)

    def run(self):
        command_string = input("Enter commands (space-separated F + -): ")
        commands = self.parser.parse(command_string)
        for cmd in commands:
            cmd.execute(self.turtle)
        self.root.mainloop()


