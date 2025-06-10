"""
sequencia de fibonacci utilizando backtracking

premisas = Fi = F(i - 1) + F(i - 2)
F1 = F2 = 1
"""

def main():
    def fibonacci(n):
        if n == 2 or n == 1:
            return 1
        
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(fibonacci(10))
    
if __name__ == "__main__":
    main()