# 5.Write a python program to count the number of vowels in the string.
str = input("Enter a String: ")
count=0
for i in str:
    if i in {"a",'e','i','o','u'}:
        count += 1
print(count)