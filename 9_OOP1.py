
############# class, properties & constructor, objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Rafy", 21)
print(f"The student {s1.name} is {s1.age} years old.")

s2 = Student("Anas", 22)
print(f"The student {s2.name} is {s2.age} years old.")

s2.age = 12
print(f"The student {s2.name} is {s2.age} years old.")

