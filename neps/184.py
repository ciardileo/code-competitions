"""
calcular
"""

def main():
    N = int(input())
    valores = [float(x) for x in input().split()]
    
    saldo = (100*valores[-1]) - (100*valores[0])
    print(f"{saldo:.2f}")

    
if __name__ == "__main__":
    main()