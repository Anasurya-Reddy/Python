n = int(input('Enter a number:'))
t=n
sum=0
while t>0:
    sum=sum+((t%10)**3)
    t = t//10
if sum==n:
    print(n,'is an Armstrong number')
else:
    print(n,'is not an Armstrong number')
