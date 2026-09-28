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
      
    grafico = [[0] * N for _ in range(H)]
    
    for i in range(N):
        for j in range(H - 1, (H-1-valores[i]), -1):
            grafico[j][i] = 1

    for linha in grafico:
        print(*linha, sep=" ")
    
    
    
if __name__ == "__main__":
    main()