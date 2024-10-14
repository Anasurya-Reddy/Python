# 9. write a python program to sum all the items in the given dictionary.
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
sum=0
for i in d.values():
    sum += i
print("Sum of items: ", sum)