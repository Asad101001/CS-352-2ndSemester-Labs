from progression import *
from arithmetic_progression import *
from geometric_progression import *
from fibonacci_progression import *


class App:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def run():
        print("\n\t\t10 iterations of Progression of increment 1 starting from 0")
        p = Progression()
        p.print_progression(10)
        print("\t\t10 iterations of Arithmetic Progression of difference 4 starting from 4")
        ap = ArithmeticProgression(4,4)
        ap.print_progression(10)
        print("\t\t10 iterations of Geometric Progression of ratio 3 starting from 1")
        gp = GeometricProgression(3,1)
        gp.print_progression(10)
        print("\t\t10 iterations of Fibonacci Progression")
        fp = FibonacciProgression()
        fp.print_progression(10)
        