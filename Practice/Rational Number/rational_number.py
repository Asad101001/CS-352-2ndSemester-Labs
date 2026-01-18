class RationalNumber:

    def __init__(self, num, deno):
        if deno == 0:
            raise ValueError("Denominator can't be zero")
        self.num = num
        self.deno = deno

    @staticmethod
    def GCD(n, d):
        while d != 0:
            n, d = d, n % d
        return n

    @staticmethod
    def LCM(n, d):
        return (n * d) // RationalNumber.GCD(n, d)

    def __add__(self, other: RationalNumber):
        new_num = self.num * other.deno + self.deno * other.num
        new_deno = self.deno * other.deno

        cancel = RationalNumber.GCD(new_num, new_deno)
        reduced_num = new_num // cancel
        reduced_deno = new_deno // cancel

        return RationalNumber(reduced_num, reduced_deno)

    def __sub__(self, other):

        new_num = self.num * other.deno - self.deno * other.num
        new_deno = self.deno * other.deno

        cancel = RationalNumber.GCD(new_num, new_deno)
        reduced_num = new_num // cancel
        reduced_deno = new_deno // cancel

        return RationalNumber(reduced_num, reduced_deno)

    def __str__(self):

        return f"The new rational number after the operation: {self.num}/{self.deno}"
