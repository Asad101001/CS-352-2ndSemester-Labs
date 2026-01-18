from progression import Progression

class FibonacciProgression(Progression):
    
    def __init__(self, first=0, second=1):
        
        super().__init__(first)
        self._previous = second - first
        
    def _advanvce(self):
        
        self._previous, self._current = self._current, self._previous + self._current
        
            

