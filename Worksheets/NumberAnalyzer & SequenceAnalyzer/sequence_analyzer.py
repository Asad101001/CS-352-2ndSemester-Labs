class SequenceAnalyzer:

    def __init__(self, data):
        self.data = data

    def minmax(self):
        smallest = largest = self.data[0]
        for item in self.data[1:]:
            if item < smallest:
                smallest = item
            elif item > largest:
                largest = item
        return (smallest, largest)

    def sum_of_squares(self):
        return sum(x * x for x in self.data)
