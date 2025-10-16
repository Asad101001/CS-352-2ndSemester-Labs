from Student import Student

class StudentList:

    def __init__(self, capacity: int = 5):
        self._capacity = capacity
        self._size = 0
        self._students: list[Student | None] = [None] * capacity
        
    def __str__(self) -> str:
        if self._size == 0:
            return "Student list is empty"
        result = "Student List:\n"
        for i in range(self._size):
            if self._students[i] is not None:
                result += str(self._students[i]) + "\n"
        return result
                   
    def expand_capacity(self):
        self._capacity *= 2
        new_array: list[Student | None] = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._students[i]
        self._students = new_array
                   
    def add_student(self, student: Student) -> bool:
        for i in range(self._size):
            if self._students[i] is not None and self._students[i]._seat_num == student._seat_num:
                print("Error: This seat number already exists") 
                return False
        if self._size == self._capacity:
            self.expand_capacity()
        self._students[self._size] = student
        self._size += 1
        return True
        
    def add_student_at(self, idx: int, student: Student) -> bool:
        if idx < 0 or idx > self._size:
            print("Error: Index out of bounds.") 
            return False
        for i in range(self._size):
            if self._students[i] is not None and self._students[i]._seat_num == student._seat_num:
                print("Error: Seat number already exists in the list!")
                return False
        if self._size == self._capacity:
            self.expand_capacity()
        for i in range(self._size, idx, -1):
            self._students[i] = self._students[i - 1]
        self._students[idx] = student
        self._size += 1
        return True    
        
    def search_student(self, key) -> int:
        for i in range(self._size):
            student = self._students[i]
            if student is None:
                continue
            if isinstance(key, int) and student._seat_num == key:
                return i
            if isinstance(key, str) and student._name.lower() == key.lower():
                return i
        return -1            
                              
    def replace_student(self, seat_num: int, new_student: Student) -> None:
        idx = self.search_student(seat_num)
        if idx == -1:
            print("Error: Seat number does not exist in the list!") 
            return
        self._students[idx] = new_student                      

    def remove_student(self, seat_num: int) -> None:                   
        idx = self.search_student(seat_num)
        if idx == -1:
            print("Error: Seat number does not exist in the list!")    
            return
        for i in range(idx, self._size - 1):
            self._students[i] = self._students[i + 1]
        self._students[self._size - 1] = None
        self._size -= 1
