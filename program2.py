def EvenOdd(n):
    if n%2==0:
        return "Even Number"
    else:
        return "Odd Number"

a = int(input("Enter a number: "))
print("Given number is ",EvenOdd(a))