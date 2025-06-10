"""
quem chegar no dia 1 = D reais por dia - 31 x D no total
a diária aumenta A reais por dia até o dia 16
quem chega no dia 2 = 30 x (D + A), dia 3 = 29 x (D + 2 x A)
https://neps.academy/br/exercise/2067
"""

def main():
    D = int(input())
    A = int(input())
    N = int(input())
    
    def calculate(D, A, N):
        days = 32 - N
        total = days * (D + A * (N-1 if N < 16 else 14))
        
        return total
    
    print(calculate(D, A, N))
      
if __name__ == "__main__":  
    main()