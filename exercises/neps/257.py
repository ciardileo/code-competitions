"""
fib(0) = fib(1) = 1
"""

def main():
    def fibonacci(n):
        if n <= 1:
            return 1
        
        return fibonacci(n-1) + fibonacci(n-2)
    
    
    N = int(input())
    
    print(fibonacci(N))
    
    
if __name__ == "__main__":
    main()