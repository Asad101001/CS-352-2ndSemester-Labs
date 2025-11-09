from change_calculator import ChangeCalculator


def test():
    c1 = ChangeCalculator(3749, 5000)

    print(c1.denominations)
    print(c1.change)
    print(c1)
    c1.display_change()

    print("\n--- After update ---")
    c1.amount_charged = 95
    print("Amount charged", c1.amount_charged)
    c1.amount_given = 500
    print("Amount given", c1.amount_given)
    c1.display_change()


if __name__ == "__main__":
    test()
