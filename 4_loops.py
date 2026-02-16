# loop for (in), while


def calculate():
    num1 = float(input("Enter number 1 : "))
    num2 = float(input("Enter number 2 : "))
    op = input("Enter Operator : (+,-,*,/) : ")

    if op == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif op == "*":
        print(f"{num1} x {num2} = {num1*num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("invalid operator")


# while True:
#     calculate()
#     doAgain = input("Do you want to perform another calculation (yes/no)?")
#     if doAgain != "yes":
#         break

# operates on a variable --> iterator
# --> st : initialization, condition, inc / dec

def generateTable():
    n = int(input("Enter a number : "))

    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i = i + 1

# while True:
#     generateTable()
#     doAgain = input("Do you print another table (yes/no)?")
#     if doAgain != "yes":
#         break


# for a in range(5):
#     print(f"a={a}")


# for a in range(5, 8):
#     print(f"a={a}")

# for a in range(34, 94, 10):
#     print(f"a={a}")

# for i in  range(30, 12, -3):
#     print(f"i={i}")


# name = "Maaz Ul Haq"
# for c in name:
#     print(f"The character is {c}")


students = ["Nousheen", "Anas", "Ammar", "Hunain"]

# for std in students:
#     print(f"{std} is 2309C1's student.")

for std in students:
    for c in std:
        print(f"The character is {c}")

