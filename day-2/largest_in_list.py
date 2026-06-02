lst = [7,5,8,26,4,26,3,22,1]

larg = lst[0]
larg2 = lst[0]

for i in range(len(lst)):
    
    if lst[i] > larg:
        #print(lst[i])
        larg2 = larg
        larg = lst[i]
    if lst[i] > larg2:
        larg2 = lst[i]
print(f"Largest: {larg}\nSecond: {larg2}")
