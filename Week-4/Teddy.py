from CuddlyToy import CuddlyToy

class Teddy(CuddlyToy):
    def __init__ ( self, size, color, job ):
        super().__init__(size)
        self.size = size
        self.color = color
        self.job = job

    def make_noise( self ):
        print("Growls!")

    def get_bio( self ):
        print (f" I am a {self.color} teddy and my job is {self.job}")

class EngineDriver(Teddy):
    def __init__(self, size):
        super().__init__(size, "Blue", "Engine Driver")


class Gardner(Teddy):
    def __init__(self, size):
        super().__init__(size,"Red","Gardner")

