from Student import Student
from StudentList import StudentList

def main():
    # Step 1: DCS creates an empty student list
    dcs = StudentList()
    print("DCS created an empty student list.\n")

    # Step 2: Students get admitted into the department
    dcs.add_student(Student(1, "Ahmed"))   # First admission
    dcs.add_student(Student(2, "Ayesha"))  # Second admission
    dcs.add_student(Student(3, "Bilal"))   # Third admission
    print("New admissions added to DCS:")
    print(dcs)

    # Step 3: Another student joins in the middle (special case)
    dcs.add_student_at(1, Student(4, "Fatima"))
    print("Fatima joined and was placed at index 1:")
    print(dcs)

    # Step 4: DCS searches for students
    idx_by_seat = dcs.search_student(2)
    print("Seat number 2 (Ayesha) found at index:", idx_by_seat)

    idx_by_name = dcs.search_student("Bilal")
    print("Bilal found at index:", idx_by_name, "\n")

    # Step 5: A student updates record (name correction or replacement)
    dcs.replace_student(3, Student(3, "Hina"))
    print("Record updated for seat 3 (Bilal replaced by Hina):")
    print(dcs)

    # Step 6: A student leaves the department
    dcs.remove_student(1)
    print("Ahmed (seat 1) left the department:")
    print(dcs)

    # Step 7: DCS checks system status
    print("Current Size:", dcs._size)
    print("Current Capacity:", dcs._capacity)
    
    print(StudentList.__dict__)

if __name__ == "__main__":
    main()
