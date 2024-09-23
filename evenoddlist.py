l = []
n = int(input("Enter the size of List:"))
print("Enter the elements into List")
for i in range(n):
	ele = int(input())
	l.append(ele)
even = []
odd = []
for i in l:
	if i%2==0:
		even.append(i)
	else :
		odd.append(i)
print("Given List:",l)
print("Even List:",even)
print("Odd List:",odd)
