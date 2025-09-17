class R3:
    def __init__(self, data):
        self.data = data

    def minmax_traditional(self):
        smallest = largest = self.data[0]
        for val in self.data[1:]:
            if val < smallest:
                smallest = val
            elif val > largest:
                largest = val
        return smallest, largest

    def minmax_pythonic(self):
        return sorted(self.data)[0], sorted(self.data)[-1]