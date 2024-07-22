a = int(input('Enter first side of triangle:'))
b = int(input('Enter second side of triangle:'))
c = int(input('Enter third side of triangle:'))
if a+b>c and b+c>a and c+a>b:
    print('It is a Valid Triangle')
else:
    print('It is a Not Valid Triangle')
