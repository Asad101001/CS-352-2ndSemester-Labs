class R2:
    def __init__(self, k):
        self.k = k

    def is_even(self):
        return (self.k & 1) == 0