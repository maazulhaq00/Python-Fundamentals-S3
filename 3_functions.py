# def greet(name):
#     print("============")
#     print(f"Hello {name}")
#     print("============")

# greet("Anas")
# greet("Saba")
# # greet() # error

# def greetWithDefaultParam(name="Person"):
#     print("============")
#     print(f"Hello {name}")
#     print("============")

# greetWithDefaultParam("Yazdan")
# greetWithDefaultParam()

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


calculate()