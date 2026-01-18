from progression import Progression

class ArithmeticProgression(Progression):
    
    def __init__(self, difference=1, start=0):
        
        super().__init__(start)
        self._difference = difference
        
    def _advanvce(self):
        
        self._current += self._difference    