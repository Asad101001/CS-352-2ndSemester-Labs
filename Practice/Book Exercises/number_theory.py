import random
import string
import sys
from typing import List, Tuple, Sequence, Iterable, Generator


class NumberTheory:
    """Handles basic number-theoretic operations."""

    @staticmethod
    def is_multiple(n: int, m: int) -> bool:
        """R-1.1: Return True if n is a multiple of m."""
        if m == 0:
            return False  # Avoid division by zero
        return n % m == 0

    @staticmethod
    def is_even(k: int) -> bool:
        """R-1.2: Check if k is even without *, %, /."""
        return (k & 1) == 0

    @staticmethod
    def sum_of_squares_less_than(n: int) -> int:
        """R-1.4: Sum of squares of positive integers < n."""
        if n <= 1:
            return 0
        return sum(i * i for i in range(1, n))

    @staticmethod
    def sum_of_odd_squares_less_than(n: int) -> int:
        """R-1.6: Sum of squares of odd positive integers < n."""
        if n <= 1:
            return 0
        return sum(i * i for i in range(1, n, 2))

    @staticmethod
    def sum_of_squares_comprehension(n: int) -> int:
        """R-1.5: One-liner using comprehension."""
        return sum(k**2 for k in range(1, n))

    @staticmethod
    def sum_of_odd_squares_comprehension(n: int) -> int:
        """R-1.7: One-liner for odd squares."""
        return sum(k**2 for k in range(1, n, 2))


class SequenceAnalyzer:
    """Analyzes sequences (lists, tuples, etc.)."""

    @staticmethod
    def minmax(data: Sequence[float]) -> Tuple[float, float]:
        """R-1.3: Return (min, max) without using built-in min/max."""
        if not data:
            raise ValueError("Sequence must be non-empty")
        smallest = largest = data[0]
        for value in data[1:]:
            if value < smallest:
                smallest = value
            elif value > largest:
                largest = value
        return smallest, largest

    @staticmethod
    def has_odd_product_pair(data: Sequence[int]) -> bool:
        """C-1.14: True if there's a distinct pair with odd product."""
        odds = [x for x in data if x % 2 != 0]
        return len(odds) >= 2

    @staticmethod
    def all_distinct(data: Sequence) -> bool:
        """C-1.15: True if all elements are unique."""
        return len(data) == len(set(data))

    @staticmethod
    def reverse(data: List) -> List:
        """C-1.13: Return reversed list (pseudo-code equivalent)."""
        reversed_list = data[:]
        left, right = 0, len(reversed_list) - 1
        while left < right:
            reversed_list[left], reversed_list[right] = (
                reversed_list[right],
                reversed_list[left],
            )
            left += 1
            right -= 1
        return reversed_list


class ListUtils:
    """Utility functions for list comprehensions and generation."""

    @staticmethod
    def powers_of_two() -> List[int]:
        """R-1.11: [1, 2, 4, 8, ..., 256]"""
        return [2**i for i in range(9)]

    @staticmethod
    def triangular_numbers() -> List[int]:
        """C-1.18: [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]"""
        return [i * (i + 1) for i in range(10)]

    @staticmethod
    def alphabet() -> List[str]:
        """C-1.19: ['a', 'b', ..., 'z'] without typing all letters."""
        return [chr(ord("a") + i) for i in range(26)]

    @staticmethod
    def range_step(start: int, stop: int, step: int) -> range:
        """Helper to generate specific ranges."""
        return range(start, stop, step)

    @staticmethod
    def negative_index_equivalent(k: int, n: int) -> int:
        """R-1.8: Convert negative index k to positive j."""
        return n + k if k < 0 else k


class RandomUtils:
    """Custom implementations of random functions."""

    @staticmethod
    def choice(data: Sequence):
        """R-1.12: Implement choice() using randrange."""
        if not data:
            raise ValueError("Sequence cannot be empty")
        index = random.randrange(len(data))
        return data[index]

    @staticmethod
    def shuffle(data: List):
        """C-1.20: In-place shuffle using only randint."""
        for i in range(len(data) - 1, 0, -1):
            j = random.randint(0, i)
            data[i], data[j] = data[j], data[i]


class StringProcessor:
    """Handles string-related operations."""

    @staticmethod
    def count_vowels(s: str) -> int:
        """C-1.24: Count vowels in a string."""
        vowels = set("aeiouAEIOU")
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def remove_punctuation(s: str) -> str:
        """C-1.25: Remove all punctuation from sentence."""
        return s.translate(str.maketrans("", "", string.punctuation))

    @staticmethod
    def reverse_lines_from_input():
        """C-1.21: Read lines until EOF, print in reverse."""
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            for line in reversed(lines):
                print(line)


class MathOperations:
    """Vector and arithmetic operations."""

    @staticmethod
    def dot_product(a: List[int], b: List[int]) -> List[int]:
        """C-1.22: Element-wise dot product (actually element-wise multiplication)."""
        if len(a) != len(b):
            raise ValueError("Arrays must have same length")
        return [a[i] * b[i] for i in range(len(a))]

    @staticmethod
    def norm(v: List[float], p: float = 2) -> float:
        """C-1.28: p-norm of a vector."""
        return sum(abs(x) ** p for x in v) ** (1 / p)


class SafeListAccessor:
    """Demonstrates safe list access with custom error message."""

    def __init__(self, data: List):
        self.data = data

    def safe_get(self, index: int):
        """C-1.23: Try to access index, catch out-of-bounds."""
        try:
            return self.data[index]
        except IndexError:
            print("Don’t try buffer overflow attacks in Python!")
            return None


class ArithmeticChecker:
    """C-1.26: Check if a, b, c satisfy any arithmetic relation."""

    @staticmethod
    def is_valid_formula(a: int, b: int, c: int) -> bool:
        return (
            a + b == c
            or a - b == c
            or b - a == c
            or a * b == c
            or (b != 0 and a // b == c)
            or (a != 0 and a == b // c)
        )


class FactorGenerator:
    """C-1.27: Efficient factor generator in increasing order."""

    @staticmethod
    def factors(n: int) -> Generator[int, None, None]:
        """Yield factors in increasing order efficiently."""
        if n <= 0:
            return
        # Find small factors
        small_factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                yield i
                if i != n // i:
                    small_factors.append(n // i)
            i += 1
        # Yield large factors in reverse
        for factor in reversed(small_factors):
            yield factor


class PermutationGenerator:
    """P-1.29: Generate all permutations of characters."""

    @staticmethod
    def permutations(chars: str) -> List[str]:
        from itertools import permutations as perm

        return ["".join(p) for p in perm(chars)]


class DivisionCounter:
    """P-1.30: Count divisions by 2 until < 2."""

    @staticmethod
    def count_divisions_by_two(n: int) -> int:
        if n <= 1:
            raise ValueError("n must be > 1")
        count = 0
        while n >= 2:
            n //= 2
            count += 1
        return count


class ChangeMaker:
    """P-1.31: Make change with minimal bills/coins (US system)."""

    DENOMINATIONS = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    @staticmethod
    def make_change(amount_due: float, amount_given: float) -> dict:
        change = amount_given - amount_due
        if change < 0:
            raise ValueError("Not enough money given")
        result = {}
        for denom in ChangeMaker.DENOMINATIONS:
            count = int(change // denom)
            if count > 0:
                result[f"${denom}"] = count
                change -= count * denom
                change = round(change, 2)  # Avoid floating point errors
        return result


class WordCounter:
    """P-1.36: Count word frequencies from input."""

    @staticmethod
    def count_words() -> dict:
        text = input("Enter words separated by spaces: ")
        words = text.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return freq


# ========================
# Example Usage / Demo
# ========================


