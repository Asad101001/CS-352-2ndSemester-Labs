from progression import Progression

class GeometricProgression(Progression):
    
    def __init__(self, ratio=2, start=1):
        
        super().__init__(start)
        self._ratio = ratio
        
    def _advanvce(self):
        
        self._current *= self._ratio  