class R7:
    def __init__(self, n):
        self.n = n

    def sum_of_odd_squares_pythonic(self):
        return sum(i*i for i in range(1, self.n, 2))