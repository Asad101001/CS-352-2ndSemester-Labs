import tkinter as tk
from Geometry.Point import Point
from Geometry.Line import Line

class TKPanel(tk.Canvas):                                       #'TKPanel' is child of 'tk.Canvas'
    def __init__(self, master=None, width=400, height=400 , **kwargs):
     super().__init__(master, width = width , height = height , bg='black', **kwargs)  #'super().__init()' shows inheritance
     self.lines = []                                            #Creating list 'lines[]' which stores 'Line' data type

    def add_line( self, p1:Point , p2:Point ):
        self.lines.append(Line(p1,p2))                          #Adding lines using append()
        self.draw()

#Visualize our objects
    def draw( self ):
        self.delete("all")                                      #Clears any previous drawing left on canvas
        for line in self.lines:
            self.create_line(line.start.get_x(), line.start.get_y(), line.end.get_x(), line.end.get_y() , fill="limegreen" ,width = 12 )
