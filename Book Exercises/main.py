from number_theory import *

if __name__ == "__main__":
    print("=== OOP Solutions Demo ===\n")

    print("R-1.1 is_multiple(10, 5):", NumberTheory.is_multiple(10, 5))
    print("R-1.2 is_even(4):", NumberTheory.is_even(4))
    print("R-1.3 minmax([3,1,4,1,5]):", SequenceAnalyzer.minmax([3, 1, 4, 1, 5]))
    print("R-1.4 sum squares < 5:", NumberTheory.sum_of_squares_less_than(5))
    print("R-1.11 powers of 2:", ListUtils.powers_of_two())
    print(
        "C-1.14 odd product pair [1,2,3,4]:",
        SequenceAnalyzer.has_odd_product_pair([1, 2, 3, 4]),
    )
    print("C-1.19 alphabet:", ListUtils.alphabet())
    print("C-1.24 vowels in 'hello':", StringProcessor.count_vowels("hello"))
    print(
        "C-1.25 remove punct:", StringProcessor.remove_punctuation("Let's try, Mike.")
    )
    print("C-1.26 valid formula 3,5,8:", ArithmeticChecker.is_valid_formula(3, 5, 8))
    print("C-1.28 norm([4,3]):", MathOperations.norm([4, 3]))
    print("P-1.29 catdog perms sample:", PermutationGenerator.permutations("cat")[:5])
    print("P-1.30 divisions for 100:", DivisionCounter.count_divisions_by_two(100))
    print("P-1.31 change for $100 given $123.45:", ChangeMaker.make_change(100, 123.45))
    print("P-1.36 word count:", WordCounter.count_words())
