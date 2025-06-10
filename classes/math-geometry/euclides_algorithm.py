"""
o algoritmo euclidiano serve para descobrir o mdc entre dois números
"""

def gcd(numbers: tuple) -> int:
    a, b = max(numbers), min(numbers)
    while b != 0:
        a, b = b, a % b
        
    return a

print(gcd((10, 45)))
        
