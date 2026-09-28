"""
N araras
M gaiolas
Arara se assusta somente se existem menos do que 4 gaiolas entre elas (desconsiderando elas próprias)
"""

def main():
    N, M = map(int, input().split())  # araras, gaiolas

    espaco_disponivel, arara_liberada = divmod(M, 5)
    N = N - 1 if arara_liberada > 0 else N

    if N > espaco_disponivel:
        print("N") 
    else:
        print("S")



if __name__ == "__main__":
    main()