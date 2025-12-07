import tkinter as tk
from Drawing.Canvas import TKPanel
from Drawing.Pen import Pen

# Tkinter setup
root = tk.Tk()
root.title("Demonstration of Pen")

##Canvas window display with lines drawn by Pen##
canvas = TKPanel(root, width=1920, height=1080)
canvas.pack()

pen = Pen(canvas)

#Making an 'A' (coordinates figured out using ChatGPT)
pen.move_to(150, 500)
pen.line_to(200, 400)
pen.line_to(250, 500)
pen.move_to(175, 450)
pen.line_to(225, 450)

root.mainloop()
        