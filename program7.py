def RevList(l):
    rl = []
    for i in l:
        rl.insert(0,i)
    return rl

list = [1,2,3,4,5,6,7,8,9]
print("Given List :", list)
print("Reversed List is ",RevList(list))
