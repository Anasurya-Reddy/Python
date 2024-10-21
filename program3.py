def GCD(m,n):
    if n==0:
        return m
    else:
        return GCD(n,m%n)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("GCD = ",GCD(a,b))