students = []

class Student:
    school_name = "SSG"

    def __init__(self, name, id=123):
        self.name = name
        self.id = id
        students.append(self)

    def __str__ (self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

vinay  = Student("vinay")
print (vinay)

print(Student.school_name)
