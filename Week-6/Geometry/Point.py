class Point:

    count = 0  # Tracks number of Point objects/instances

#NULL / DEFAULT Constructor

    #Point() -> x=0,y=0
    def __init__ ( self, x = 0.0, y = 0.0 ):  # Default constructor if user does not provide any argument.

#PARAMETRIZED Constructors

        #Copy constructor
        #Point(A) -> x=A.x,y=A.y
        if isinstance (x, Point):           # Checks if argument entered already is an instance of Point class
            self._x = x._x
            self._y = x._y

        else:

        #Two-parameter constructor
        #Point(x,y) -> x,y
            self._x = x
            self._y = y

        Point.count += 1

# Tried using @property and @setters as decorators to treat attributes as functions to ensure encapsulation
    # @property
    # def x( self ):
    #     return self._x
    # @x.setter
    # def x(self, value):
    #    self._x = value
    #
    # @property
    # def y(self):
    #    return self._y
    #
    # @y.setter
    # def y(self, value):
    #    self._y = value

# But then setter() and getter() are not callable leading to code breaking

#NEW Setters
    def set_x( self,value ):
        self._x = value
    def set_y( self, value ):
        self._y = value

#NEW Getters
    def get_x( self ):
        return self._x
    def get_y( self ):
        return self._y


    #ADDITION OF 2 POINTS
    def add ( self, other ):

        if isinstance (other, Point):
            return Point (self._x + other._x, self._y + other._y)
        raise TypeError ("Can only add Point to Point")

    #OPERATOR OVERLOADING

    #Addition
    def __add__ ( self, other ):
        return self.add (other)

    #String magic functions

    def __str__ ( self ):
        return f"({self._x}, {self._y})"

    def __repr__ ( self ):
        return f"Point(x={self._x}, y={self._y})"

    # === Equality override ===
    def __eq__ ( self, other ):
        return isinstance (other, Point) and self._x == other._x and self._y == other._y

    def distance ( self, p ):
        return ((self._x - p._x) ** 2 + (self._y - p._y) ** 2) ** 0.5

    # @classmethod to get total instances/objects
    @classmethod
    def get_count ( cls ):
        return cls.count
