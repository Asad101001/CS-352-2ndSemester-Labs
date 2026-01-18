class LoggerMixin:
    def describe(self):
        return "Logging polygon info"


class Polygon:
    def describe(self):
        return "Generic Polygon"


class RegularPolygon(Polygon, LoggerMixin):
    def describe(self):
        result = super().describe()
        return f"{result} -> Regular Polygon"


class Square(RegularPolygon):
    pass


shape = Square()
print(shape.describe())

print(Square.__mro__)


##  Generic Polygon -> Regular Polygon

## REASONING
## MRO -> (<class '__main__.Square'>, <class '__main__.RegularPolygon'>, <class '__main__.Polygon'>,
#                                                  <class '__main__.LoggerMixin'>, <class 'object'>)
