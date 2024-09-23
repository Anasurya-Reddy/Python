l = []
n = int(input("Enter the size of list:"))
print("Enter the elements into list")
for i in range(n):
	ele = int(input())
	l.append(ele)
l.reverse()
print(l)
