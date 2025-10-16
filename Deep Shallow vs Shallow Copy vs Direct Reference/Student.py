class Student:
    
    def __init__(self, name: str):
        self._name = name
        
    def __repr__(self):
        return f"Student Name: ({self._name!r})" 
    
    def clone(self):
        return Student(self._name)   
    
    def __setitem__(self):
        return self
    
    @property
    def name(self, index):
        return self._name[index]
    @name.setter
    def name(self, index, value):
        self._name[index] = value