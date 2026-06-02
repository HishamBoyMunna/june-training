stars = int(input())
prev = 0
for i in range(stars):
    current = (10**(i)) + prev 
    prev = current
    print(current*(i+1))
