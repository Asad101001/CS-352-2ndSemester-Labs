class FactorDemo:

    def __init__(self, n):
        self.n = n

    # Return with value (legal now, but silent)
    def bad_generator_mix(self):
        for k in range(1, self.n + 1):
            if self.n % k == 0:
                if k > 10:
                    return "Too big"
                yield k

    # Logical error (still compiles but wrong)
    def bad_generator_logic(self):
        results = []
        for k in range(1, self.n + 1):
            if self.n % k == 0:
                results.append(k)
                yield results  # yields growing list increasing memory consumption

    # Correct generator
    def good_generator(self):
        for k in range(1, self.n + 1):
            if self.n % k == 0:
                yield k
