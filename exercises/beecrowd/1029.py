"""
fibonacci simples
"""

import sys
sys.setrecursionlimit(1000000)

dp = dict()

def fibo(n: int):
    if dp.get(n, -1) == -1:
        dp[n] = fibo(n - 1) + fibo(n - 2)

    return dp[n]


# 1 0 0
# 2 2 2
# 3 4 4
# 4 8 6
# 5 14 8
# 6 

def main():
    N = int(input())  # número de casos
    dp[1] = 1
    dp[0] = 0

    for _ in range(N):
        X = int(input())  # posição na sequência de fibo
        result = fibo(X)
        num_calls = 2 * fibo(X+1) - 2
        print(f"fib({X}) = {num_calls} calls = {result}")

if __name__ == "__main__":
    main()