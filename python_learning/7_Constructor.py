students = []

class Student:
    def __init__(self, name, id=123):
        student = {"Name": name, "ID": id}
        students.append(student)

    def __str__ (self):
        return "Studenti class"

vinay  = Student("vinay")
print (vinay)
print(students)
