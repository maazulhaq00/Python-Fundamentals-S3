# take a number as user input, check if number is even or odd

num1 = int(input("Enter a number : "))

# if num1 % 2 == 0:
#     print(f"{num1} is even.")
# else:
#     print(f"{num1} is odd.")

# short hand if-else
# (block if true) if (cond) else (block if false) 

print(f"{num1} is even.") if num1%2==0 else print(f"{num1} is odd.")
