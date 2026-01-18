from StudentList import StudentList
from Student import Student

list1 = StudentList()

s1 = Student("Asad")
s2 = Student("Rizwan")

list1.add_student(s1)
list1.add_student(s2)

direct_ref = list1.get_students("direct")
shallow_ref = list1.get_students("copy")
deep_ref = list1.get_students("deep")

print("original list:", list1._students)
print("direct reference:", direct_ref)
print("shallow ref:", shallow_ref)
print("deep ref:", deep_ref)

list1._students[0]._name = "changed"

print("After modification changes:")
print("original list:", list1._students)
print("direct reference:", direct_ref)
print("shallow ref:", shallow_ref)
print("deep ref:", deep_ref)
