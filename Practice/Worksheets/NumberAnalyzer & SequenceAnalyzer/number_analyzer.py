class NumberAnalyzer:

    def __init__(self, value: int):
        self.value = value

    def is_multiple_of(self, m: int) -> bool:
        return self.value % m == 0

    def is_even(self) -> bool:
        return (self.value & 1) == 0

    def sum_of_squares_below(self) -> int:
        total = 0
        for i in range(1, self.value):
            total += i * i
        return total

    def sum_of_odd_squares(self) -> int:
        total = 0
        for i in range(1, self.value, 2):
            total += i * i
        return total
