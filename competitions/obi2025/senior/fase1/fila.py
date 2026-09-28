"""
N alunos dispostos em 1 fila
Cadeira i1 fica no fundo da sala e cadeira iN fica em frente ao professor.
a: altura em centímetros

Retornar a quantidade de alunos que não poderá ser visto
"""

def main():
    N = int(input())  # quantidade de alunos
    alunos = list(map(int, input().split()))  # de i1 a iN
    maior = alunos[N - 1]
    resultado = 0
    
    for i in range(N - 2, -1, -1):
        if (alunos[i] <= maior):
            resultado += 1
        else:
            maior = alunos[i]    
    
    print(resultado)    
    
    
if __name__ == "__main__":
    main()