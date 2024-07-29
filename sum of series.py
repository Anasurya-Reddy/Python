n = int(input('Enter a number:'))
sum=0
f=1
for i in range(1,n+1):
    f = f*i
    x=i/f
    sum=sum+x
print(sum)
