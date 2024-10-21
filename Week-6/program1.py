def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Sum = ",add(a,b))
print("Difference = ",sub(a,b))
print("Product = ",multi(a,b))
print("Quotient = ",div(a,b))
