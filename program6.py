# 6.Write a python program to print even length words in a string.
str = input("Enter a String: ").split()
for i in str:
    if len(i)%2==0:
        print(i)