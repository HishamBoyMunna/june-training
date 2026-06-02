lst = [5,7,6,8,2,3,1]
lst2 = [6,4,7,3,5,4,1]
lst3 = []
for i in range(len(lst)):
    lst3.append(lst[i]+lst2[len(lst2)-1-i])

print(lst3)
