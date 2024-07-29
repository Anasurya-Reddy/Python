n = int(input('Enter a number:'))
t = n
sum=0 
while t>0:
    sum=(sum*10)+(t%10)
    t=t//10
if sum==n:
    print(n,'is a Palindrome number')
else:
    print(n,'is not a Palindrome number')
