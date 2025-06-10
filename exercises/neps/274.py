"""
algoritmo de euclides para fazer mdc
o mdc de a, b e c é igual ao mdc do mdc entre a e b, e c
"""

def main():
    def mdc(num1, num2):
        a, b = max(num1, num2), min(num1, num2)
        while b != 0:
            a, b = b, a % b
        
        return a
    
    N = int(input())
    
    numeros = [int(x) for x in input().split()]
    
    result = mdc(numeros[0], numeros[1])
    
    for i in range(2, N):
        result = mdc(result, numeros[i])
        
    print(result)
    
    
if __name__ == "__main__":
    main()