"""
Matrix NxM
N e M ímpares
Todo par de cookies adjascentes devem ter soma ímpar
Determinar a quantidade mínima de gotas que devem ser adicionadas
Descrever a configuração final também
===
Números ímpares devem ser exclusivamente cercados por pares, e números pares devem ser exclusivamente cercados por ímpares

3 2 3 2
2 3 2 3
2 2 2 2
2 2 2 2


I P I
P P P 
I P I

P I P I P
I P I P I
P I P I P
I P I P I
P I P I P

P P P P P
I I P P P
P P P P P
P P P I I
I I I I P



P I P I P
I P I P I
P I P I P
I P I P I
P I P I P
"""


def main():
    N, M = map(int, input().split())
    bandeja = []

    for _ in range(N):
        bandeja.append(list(map(int, input().split())))




if __name__ == "__main__":
    main()