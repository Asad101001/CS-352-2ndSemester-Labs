from Student import Student
from copy import deepcopy


class StudentList:
    
    def __init__(self, capacity: int=3):
        self._capacity = capacity
        self._students : list[Student|None] = [None] * capacity
    
        
    def add_student(self, student:Student):
        self._students.append(student)
        
    def get_students(self, mode:str = "direct"):
        if mode == "direct":
            return self._students
        
        elif mode == "copy":
            return self._students.copy()
        
        elif mode == "deep":
            return deepcopy(self._students)    
        
        else:
            raise ValueError("mode must be direct/copy/deep")
        
