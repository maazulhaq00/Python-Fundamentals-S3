
############# methods

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"The student {self.name} is {self.age} years old.")


s1 = Student("Rafy", 21)
s2 = Student("Anas", 22)

s1.show_info()
s2.show_info()

Student.show_info(s1)
Student.show_info(s2)
