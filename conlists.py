list1 = ["M", "na", "i", "Abhi"]
list2 = ["y", "me", "s", "ram"]
output = []
for i in range(min(len(list1),len(list2))):
	ele = list1[i]+list2[i]
	output.append(ele)
print(output)
