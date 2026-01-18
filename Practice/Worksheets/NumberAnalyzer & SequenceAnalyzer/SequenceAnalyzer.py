class SequenceAnalyzerUpgraded:

    def __init__(self, sequence):
        self._sequence = list(sequence)

    """Analyze numerical sequences using object-oriented and Pythonic methods."""

    # --- Basic Properties ---
    def get_sequence(self):
        """Return the stored sequence."""
        return self._sequence

    def length(self):
        """Return number of elements in the sequence."""
        return len(self._sequence)

    # --- R-1.3: Find smallest and largest manually (no min/max) ---
    def minmax(self):
        """Return (min, max) without using built-in min() or max()."""
        if not self._sequence:
            raise ValueError("Sequence is empty.")
        smallest = largest = self._sequence[0]
        for value in self._sequence[1:]:
            if value < smallest:
                smallest = value
            elif value > largest:
                largest = value
        return smallest, largest

    # --- R-1.4 / R-1.7: Distinctness and uniqueness ---
    def distinct_count(self):
        """Return how many distinct elements exist."""
        return len(set(self._sequence))

    def is_unique(self):
        """Return True if all elements are distinct."""
        return len(set(self._sequence)) == len(self._sequence)

    # --- R-1.5 / R-1.6: Sum of squares, and odd squares ---
    def sum_of_squares(self):
        """Return sum of squares of all numbers."""
        return sum(x * x for x in self._sequence)

    def sum_of_odd_squares(self):
        """Return sum of squares of all odd numbers."""
        return (sum(x * x for x in self._sequence if x % 2 == 1) , self.is_unique())

    # --- C-1.14: Check if any pair product is odd ---
    def has_odd_product_pair(self):
        """Return True if there exists a distinct pair (a, b) whose product is odd."""
        n = len(self._sequence)
        for i in range(n):
            for j in range(i + 1, n):
                if (self._sequence[i] * self._sequence[j]) % 2 == 1:
                    return True
        return False

    # --- C-1.15: Check if all numbers are distinct ---
    def all_distinct(self):
        """Return True if all numbers differ (same as is_unique)."""
        return self.is_unique()

    # --- Utility methods for comprehension practice ---
    def reversed_view(self):
        """Return a reversed version of the sequence."""
        return self._sequence[::-1]

    def even_elements(self):
        """Return a list of even elements."""
        return [x for x in self._sequence if x % 2 == 0]

    def squares_list(self):
        """Return a list of all squares."""
        return [x * x for x in self._sequence]

    def squares_generator(self):
        """Yield squares lazily (demonstrates generator concept)."""
        for x in self._sequence:
            yield x * x
