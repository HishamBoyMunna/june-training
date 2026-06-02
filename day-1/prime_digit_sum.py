import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

number = int(input("Enter the number: "))
len = int(math.log10(number) + 1) 
print(len)

part_a = number // 10 
part_b = number % 10 
sum = 0
while(part_a):
    print(part_a,part_b)
    part_b = part_a % 10
    part_a //= 10 
    if(is_prime(part_b)):
        sum += part_b
print(0,part_b)
if(is_prime(part_a)):
    sum += part_a
print(sum)
    


