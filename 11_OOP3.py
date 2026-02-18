
############# list of objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"The student {self.name} is {self.age} years old.")


students_list = [
    Student("Nousheen", 18), Student("Ammar", 22), Student("Saba", 21), Student("Wasiq", 19)
]

students_list[1].show_info()

for obj in students_list:
    obj.show_info()