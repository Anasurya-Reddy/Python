l = []
n = int(input("Enter the size of List:"))
print("Enter the elements into List")
for i in range(n):
	ele = int(input())
	l.append(ele)
temp = l[0]
l[0] = l[-1]
l[-1] = temp
print(l)
