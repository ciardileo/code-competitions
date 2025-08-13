"""
Objetivo: encontrar o número de trios de palitos distintos que formem um triângulo
Estratégia:

"""

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def main():
    N = int(input())  # número de palitinhos
    palitos = list(map(int, input().split()))
    total = 0
    
    # forma todos os trios possíveis
    for i in range(len(palitos)):
        for j in range(i + 1, len(palitos)):
            for k in range(j + 1, len(palitos)):
                if is_triangle(palitos[i], palitos[j], palitos[k]):
                    total += 1
    
    print(total)
    
if __name__ == "__main__":
    main()