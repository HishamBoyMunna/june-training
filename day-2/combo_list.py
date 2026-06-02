lst = [4,7,5,9,3,4]

for i in lst[:len(lst)-1]:
    for j in lst[lst.index(i)+1:]:
        print(f"{i}{j}",end=" ")

