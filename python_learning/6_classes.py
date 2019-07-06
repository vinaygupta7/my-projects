students = []

class Student:
    def add_student(self, name, id=123):
        student = {"Name": name, "ID": id}
        students.append(student)

student = Student()
student.add_student("Vinay")
print (students)
