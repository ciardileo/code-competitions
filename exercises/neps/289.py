"""
ilhas numeradas de 1 a N
no programa há duas interações:
    1 - o engenheiro está informando que tem uma conexão entre a ilha A e B
    0 - o prefeito pergunta se há uma conexão entre A e B
"""

from collections import defaultdict

def main():
    ilhas, interacoes = [int(x) for x in input().split()]
    mapa = defaultdict(set)
    result = []
    
    for _ in range(interacoes):
        tipo, ilha1, ilha2 = [int(x) for x in input().split()]
        
        if tipo == 0:
            # pergunta do prefeito
            if ilha2 in mapa[ilha1]:
                result.append(1)
            else:
                result.append(0)
        else:
            # informação do secretário
            mapa[ilha1].add(ilha2)
            mapa[ilha2].add(ilha1)
    
    # mostrar a saída das perguntas
    print(*result, sep='\n')
                

if __name__ == "__main__":
    main()