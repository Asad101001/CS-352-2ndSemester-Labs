from Person import Person

class Student(Person):
    
    def __init__(self, seat_num: int, name: str):
        super().__init__(name)
        self._seat_num = seat_num
        
    def __str__(self) -> str:
        return f"{super().__str__()} with seat #: {self._seat_num}"
