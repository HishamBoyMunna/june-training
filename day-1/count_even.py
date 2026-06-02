number = int(input())

length = len(str(number)) #use log10 for count
sum = 0
part_a = 0
while(part_a>=0):
    part_a = number // 10
    part_b = number % 10
    sum += part_b ** length 
    length -= 1

    
print(sum)



