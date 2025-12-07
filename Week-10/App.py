from Exercises import *
class App:
    def __init__(self):
        pass

    @staticmethod
    def run():
        print ("==== R-1.1 ====")
        q1a = R1 (60, 6)
        print (q1a.is_multiple ())
        q1b = R1 (60, 7)
        print (q1b.is_multiple ())

        print("==== R-1.2 ====")
        q2a = R2(10)
        print("10 even? ->", q2a.is_even())
        q2b = R2(11)
        print("11 even? ->", q2b.is_even())

        print("==== R-1.3 ====")
        q3 = R3([7, 2, 9, 4, 1, 5])
        print("Traditional:", q3.minmax_traditional())
        print("Pythonic:", q3.minmax_pythonic())

        print("==== R-1.4 ====")
        q4 = R4(6)
        print("Traditional:", q4.sum_of_squares())
        print("Pythonic:", q4.sum_of_squares_pythonic())

        print("==== R-1.5 ====")
        q5 = R5(6)
        print("Pythonic:", q5.sum_of_squares())

        print("==== R-1.6 ====")
        q6 = R6(10)
        print("Traditional:", q6.sum_of_odd_squares())

        print("==== R-1.7 ====")
        q7 = R7(10)
        print("Pythonic:", q7.sum_of_odd_squares_pythonic())

        print("==== R-1.8 ====")
        q8 = R8("python", -2)
        print("Equivalent index for s[-2]:", q8.equivalent_index())

        print("==== R-1.9 ====")
        q9 = R9()
        print("Range:", q9.get_range())

        print("==== R-1.10 ====")
        q10 = R10()
        print("Range:", q10.get_range())

        print("==== R-1.11 ====")
        q11 = R11()
        print("List:", q11.generate_list())

        print("==== R-1.12 ====")
        q12 = R12([10, 20, 30, 40, 50])
        print("Random choice:", q12.custom_choice())

        print("==== P-1.35 ====")
        bp = BirthdayParadox(trials=5000)
        results = bp.birthday_paradox()
        for n, prob in results.items():
            print(f"n={n}: probability={prob:.3f}")

        
        print("==== P-1.36 ====")
        wc = WordCounter("apple orange apple banana apple orange")
        print("Word counts:", wc.word_counter())





        