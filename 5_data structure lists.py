# --------- list: ordered, mutable, indexed, duplicate values can be stored
fruits = ["mango", "watermelon", "gauva"]

print(fruits)
print(len(fruits))

fruits.append("banana")
print(fruits)

fruits.insert(3, "apple")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("gauva")
print(fruits)

fruits[1] = "water melon"
print(fruits)

# fruits[15] = "orange" # out of range error
# print(fruits)

for f in fruits:
    print(f"{f} is fruit.")

print("apple" in fruits)
print("grapes" in fruits)


