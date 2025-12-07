from P36 import P36

class App:
    def __init__(self):
        pass

    def run(self):
        obj = P36("Asad is a CS student")
        print("==== P-1.36 Word Counter ====")
        print("Word counts:", obj.count_words())
