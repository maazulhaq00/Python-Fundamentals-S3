# --------- dictionaries : key-value pair
product1 = {
    "title": "Eco friendly water bottle",
    "price": 1500,
    "rating": 8.3,
    "colors": ["Green", "Black", "Pink"],
    "onDiscount": False
}

print(product1)
print(product1["title"])
# print(product1["stock"]) # error

print(product1.get("title"))
print(product1.get("Stock"))

# adding new prop / key-value pair
product1["stock"] = 22
print(product1)

print(len(product1))

print("title" in product1) # True
print("stock" in product1) # True
print("discount" in product1) # False

print(product1["colors"][1])
print(product1.get("colors")[1])

for key in product1:
    print(f"The {key} is {product1[key]}")