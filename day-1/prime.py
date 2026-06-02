def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False      
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
                
    return [p for p in range(2, limit + 1) if sieve[p]]

limit = int(input("Enter the limit: "))
print(sieve(limit)) 
