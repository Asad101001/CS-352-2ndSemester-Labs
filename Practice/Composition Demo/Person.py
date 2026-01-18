class Person:
    
    def __init__(self, name: str):
        self._name = name
        
    def __str__(self) -> str:
        return f"Name: {self._name}"  