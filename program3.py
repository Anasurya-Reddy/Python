# 3.Write a python program to che k if the given string is palindrome or not.
str = input("Enter a Sring: ")
rev = str[::-1]
if str == rev :
    print("Given string is a palindrome")
else :
     print("Given string is a not palindrome")