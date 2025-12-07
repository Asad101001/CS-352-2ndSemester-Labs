class R1:
    def __init__ ( self, n, m ):
        self.n = n
        self.m = m

    def is_multiple ( self ):
        i = 0
        while i * self.m <= self.n:
            if i * self.m == self.n:
                return True
            i += 1
        return False

