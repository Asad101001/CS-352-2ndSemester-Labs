class R8:
    def __init__(self, s, k):
        self.s = s
        self.k = k

    def equivalent_index(self):
        n = len(self.s)
        return n + self.k  # since k < 0