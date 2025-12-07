from Geometry.Point import Point

A = Point()
B = Point (6, 9)
print("Point B's original values of x :",B.get_x() , " and y :", B.get_y())
B.set_x(7)
B.set_y(11)
C = Point(B)
D = Point(4,1)
E = C.__add__(D)
print("Point B's altered values of x:",B.__str__())
print("New Point D :",D.__str__())
print("Point E = A + D : ", E)
