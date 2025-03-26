"""
cada delegação tem vários grupos de K = 1 pessoas
a minha delegação pode levar até M
a rival vai levar N
o MDC entre o número N e X tem que ser 1, achar o maior número primo entre 1 e M, esse é o X
"""

def main():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    
    N, M = [int(x) for x in input().split()]
    
    for x in range(M, 0, -1):
        if gcd(N, x) == 1:
            print(x)
            return
    
    
if __name__ == "__main__":
    main()