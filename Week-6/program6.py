def flatList(l):
    fl = []
    for i in l:
        for j in i:
            fl.append(j)
    return fl

list = [[1,2,3],[4,5],[6,7,8,9]]
print("Given List :", list)
print("Flattened List is ",flatList(list))