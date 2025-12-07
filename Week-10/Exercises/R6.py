class R6:
    def __init__(self, n):
        self.n = n

    def sum_of_odd_squares(self):
        total = 0
        for i in range(1, self.n, 2):
            total += i * i
        return total

    def sum_of_odd_squares_pythonic(self):
        return sum(i*i for i in range(1, self.n, 2))