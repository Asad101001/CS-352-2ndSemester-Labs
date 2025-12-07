from CuddlyToy import CuddlyToy

class Bunny(CuddlyToy):
    def __init__(self, size, color,job):
        super().__init__(size)
        self.size = size
        self.color = color
        self.job  =job

    def make_noise( self ):
        print("Squeak!")

    def get_bio( self ):
        print (f" I am a {self.color} teddy and my job is {self.job}")

class Clown(Bunny):
    def __init__(self, size):
        super().__init__(size, "White", "Clown")
  
class BankManager(Bunny):
    def __init__(self, size):
        super().__init__(size, "Black", "Bank Manager")