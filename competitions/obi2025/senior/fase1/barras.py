"""
N opções de brinquedo
Xi indica quantos participantes preferem o i-ésimo brinquedo
Gráfico deve ter N colunas e altura H
H é o maior Xi da lista
"""

def main():
    N = int(input())
    valores = list(map(int, input().split()))
    H = max(valores)  # altura dos gráficos
    
    grafico = [[0] * (H - x) + [1] * x for x in valores]    
    grafico_transposto = [[0] * N for _ in range(H)]
    
    for i in range(0, N):
        for j in range(0, H):
            grafico_transposto[j][i] = grafico[i][j]
        
    for linha in grafico_transposto:
        print(*linha, sep=" ")
    
    
    
if __name__ == "__main__":
    main()