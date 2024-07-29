n=int(input('Enter a number:'))
print('Multiplication table using for loop for ',n)
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

print('Multiplication table using whlie loop for ',n)
j = 1
while j<=10:
    print(f"{n} X {j} = {n*j}")
    j=j+1
