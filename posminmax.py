l = []
n = int(input("Enter the size of List:"))
print("Enter the elements into List")
for i in range(n):
	ele = int(input())
	l.append(ele)
print("Index of Minimum value:",l.index(min(l)))
print("Index of Maximum value:",l.index(max(l)))
