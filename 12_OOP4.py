
############# user input for list of objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"The student {self.name} is {self.age} years old.")


students_list = []

for i in range(4):
    n = input("Enter a student's name: ")
    a = int(input("Enter a student's age: "))
    students_list.append(Student(n, a))

for obj in students_list:
    obj.show_info()