from polygon import Polygon


class IrregularPolygon(Polygon):

    def __init__(self, vertices):
        super().__init__(vertices)

    def area(self):
        n = self.n
        x = [p.x for p in self.vertices]
        y = [p.y for p in self.vertices]
        return 0.5 * abs(
            sum(x[i] * y[(i + 1) % n] - y[i] * x[(i + 1) % n] for i in range(n))
        )

    def __str__(self) -> str:
        return (
            f"IrregularPolygon with {self.n} vertices,"
            f"Perimeter={self.perimeter():.2f},"
            f"Area={self.area():.2f}"
        )
