from abc import abstractmethod,ABC


class CuddlyToy:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def make_noise( self ):
        pass

    @abstractmethod
    def get_bio( self ):
        pass