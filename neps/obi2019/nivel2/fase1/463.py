"""
idade dos 3 filhos somada é igual a da mãe
"""

def main():
    M = int(input())
    A = int(input())
    B = int(input())
    
    C = M - A - B
    
    print(max(C, B, A))
    
    
if __name__ == "__main__":
    main()