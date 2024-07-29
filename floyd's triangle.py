n = int(input('Enter number of rows:'))
k = 1
for i in range(n+1):
    for j in range(i):
        print(k,end=" ")
        k = k+1
    print()
