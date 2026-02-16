# --------- tuple: ordered, immutable, indexed, duplicate values can be stored
grades = ("DISTINCTION", "CREDIT", "PASS", "FAIL")

print(grades)
print(grades[2])
print(len(grades))

# grades.append("I-grade") # error
# grades.remove("PASS") # error
# grades[0] = "DIST" # error

# tuple unpacking
student = ("Anas", 21, "Karachi")

# name = student[0]
# age = student[1]
# city = student[2]

name, age, city = student

print(f"Hello, {name}, your age is {age}, you live in {city}.")

print("Anas" in student)
print("Lahore" in student)

for detail in student:
    print(detail)


sizes = "Small", "Medium", "Large"

print(sizes)
