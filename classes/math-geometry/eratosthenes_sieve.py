"""
função do crivo de eratosthenes, serve para encontrar todos os números primos de um intervalo
"""

def eratosthenes_sieve(limit):
    prime = [True for _ in range(limit + 1)]
    
    number = 2
    while number ** 2 <= limit:
        if prime[number]:
            for i in range(number ** 2, limit + 1, number):
                prime[i] = False
                
        number += 1 
    
    prime_numbers = [x for x in range(2, limit + 1) if prime[x]]
    
    return prime_numbers

print(eratosthenes_sieve(1000))