import random

class R12:
    def __init__(self, data):
        self.data = data

    def custom_choice(self):
        idx = random.randrange(len(self.data))
        return self.data[idx]