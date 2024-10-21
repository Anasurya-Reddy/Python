def SecLarge(l):
    l.sort()
    return l[-2]


list = [1,2,3,4,5,6,7,8,9]
print("Given List :", list)
print("Second Largest Number in given List is ",SecLarge(list))