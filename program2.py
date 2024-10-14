# 2.Write a python program to reverse a given string without using a slicing operator.
str = input("Enter a String: ")
rev = ""
for i in str:
    rev = i + rev
str = rev
print(str)