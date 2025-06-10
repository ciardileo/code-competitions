"""
achar o maior número entre N e M que a soma dos digitos seja S
https://neps.academy/br/exercise/2071
"""

def main():
    N = int(input())
    M = int(input())
    S = int(input())
    
    def find_highest_number():
        for num in range(M, N, -1):
            total = 0
            for alg in str(num):
                total += int(alg)
                
            if total == S:
                return num
        
        return - 1
    
    print(find_highest_number())
            
    
    
if __name__ == "__main__":
    main()