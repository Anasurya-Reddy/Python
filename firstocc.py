l = []
n = int(input("Enter the size of List:"))
print("Enter the elements into List")
for i in range(n):
	ele = int(input())
	l.append(ele)
a = int(input("Enter an element to remove first occurence:"))
l.remove(a)
print(l)
