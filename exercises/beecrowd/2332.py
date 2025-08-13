"""
malha quadriculada N x M
altura de 0 a 9
inicio em 0, 0
chegar a saída N, M
movimentação em 4 direcões, não consegue mover se a altura foi maior que 1
cada célula aumenta sua altura até 9 e quando bate vai para a 0, toda rodada

# solução 1: tentar todas as possibilidades, pois o tamanho máximo da matriz é 2500
- bfs "normal", porém também tem a opcão de esperar (adicionando a própria posição de folta na fila) SE e SOMENTE SE houver algum de seus vizinhos válidos que ainda não foi visitado. Agora, o nível atual tem que ser calculado com base nas rodadas: (original + rodadas) % 9
o ciclo se repete de 10 em 10 rodadas, então eu posso calcular todas as possibilidades de posições, que seriam no máximo 50 x 50 x 10 = 25000
"""

from collections import deque
   
def bfs(matriz, objetivo):
    visitados = set()  # evita o loop infinito de repetições
    fila = deque([[0, 0, 0]])  # próximos a serem visitados + quantidade de rodadas até aqui
    movimentos = ((1, 0), (-1, 0), (0, 1), (0, -1))  # cima baixo direita esquerda
    visitados.add((0, 0, 0))  # posição, rodada nessa posição
    # resultado = float('inf')
    
    while fila:
        # pega a posição atual e calcula o nível com base no número de rodadas
        row_atual, col_atual, rodadas = fila.popleft()
        # print(f"Rodada {rodadas}: estou na posição {row_atual}, {col_atual}")
        nivel_pos_atual = (matriz[row_atual][col_atual] + rodadas) % 10

        # para todos os movimentos possíveis
        for x, y in movimentos:
            row_novo = row_atual + x
            col_novo = col_atual + y
            
            # se o movimento está dentro dos limites
            if 0 <= row_novo <= objetivo[0] and 0 <= col_novo <= objetivo[1]: 
                # se essa nova posição ainda não foi visitada nessa rodada 
                if (row_novo, col_novo, rodadas % 10) not in visitados:
                    # calcula o nível atual
                    nivel_pos_novo = (matriz[row_novo][col_novo] + rodadas) % 10
                    
                    if nivel_pos_novo - 1 <= nivel_pos_atual:  # se é possível pular
                        if (row_novo, col_novo) == objetivo:  # se for o objetivo
                            # resultado = min(resultado, rodadas + 1)
                            return rodadas + 1
                            
                        # adicionar para ser checado
                        # print(f"Vou visitar {row_novo}, {col_novo}")
                        fila.append((row_novo, col_novo, rodadas + 1))
                        visitados.add((row_novo, col_novo, (rodadas + 1) % 10))  
        
        # adição do movimento de ficar parado
        if (row_atual, col_atual, (rodadas + 1) % 10) not in visitados:
            fila.append((row_atual, col_atual, rodadas + 1))
            visitados.add((row_atual, col_atual, (rodadas + 1) % 10))

    return -1    

def main():
    N, M = [int(x) for x in input().split()]  # linhas, colunas
    matriz = []
    
    for _ in range(N):
        matriz.append([int(x) for x in input().split()])
        
    # print(*matriz, sep='\n')
    
    print(bfs(matriz, (N - 1, M - 1)))

if __name__ == "__main__":
    main()