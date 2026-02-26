class Calculator:
    def add(self, a, b, c=0, d=0): # default arguments
        return a + b + c + d
    
    def addition(self, *numbers): # *args
        return sum(numbers)
    


c1 = Calculator()
print(c1.add(2,3))
print(c1.add(4,6,8))
print(c1.add(4,9,8,1))

print(c1.addition(1,2,3))
print(c1.addition(55,66,71, 15, 18, 66, 54))