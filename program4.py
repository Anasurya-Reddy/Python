# 4.Write a python program to find the length of the string without using the len() method.
str = input("Enter a String: ")
count=0
for i in str:
    count += 1
print(count)