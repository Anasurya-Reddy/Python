l = []
n = int(input("Enter the size of List:"))
print("Enter the elements")
for i in range(n):
	ele = int(input())
	l.append(ele)
print("Elements in the List is :",l)
print("Sum =",sum(l))
print("Average =",sum(l)/len(l))
