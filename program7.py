# 7.Write a program to check if a given key exists in a dictionary or not.
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
key = input("Enter the key: ")
flag=0
if key in d:
        print("Your key is found in Dictionary")
        flag=1
if flag==0:
    print("Your key not found")