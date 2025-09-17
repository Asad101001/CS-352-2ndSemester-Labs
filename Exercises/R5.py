class R5:
    def __init__(self, n):
        self.n = n

    def sum_of_squares(self):
        return sum(i*i for i in range(1, self.n))