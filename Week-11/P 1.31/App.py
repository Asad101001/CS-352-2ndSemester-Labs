from P31 import P31

class App:
    def __init__(self):
        pass

    @staticmethod
    def run():
            obj1 = P31(678,1000)
            obj2 = P31(500, 300)
            obj3 = P31("abc", 1000)
            obj4 = P31(-100, 500)
            print("==== P-1.31 make_change ====")
            print("Case 1 (Valid - charged:678, given:1000):", obj1.make_change())
            print("Case 2 (Insufficient - charged:500, given:300):", obj2.make_change())
            print("Case 3 (TypeError - charged:abc, given:1000):", obj3.make_change())
            print("Case 4 (Negative - charged:-100, given:500):", obj4.make_change())