""" 
retornar se a música existe e qual é seu nome, ou se não, escrever "Nao existe musica"
"""

def main():
    def find_song(notas):
        return musicas.get(notas, "Nao existe musica")
    
    N, Q = [int(x) for x in input().split()] # musicas conhecidas, quantas musicas ele vai tocar
    musicas = dict() # músicas conhecidas
    resultado = []
    
    # adiciona as músicas conhecidas
    for _ in range(N):
        dados = input().split()
        nome = dados[0]
        notas = tuple(dados[1:])
        
        musicas[notas] = nome
        
    for _ in range(Q):
        notas = tuple(input().split())
        resultado.append(find_song(notas))
        
    print(*resultado, sep='\n')
        
    
if __name__ == '__main__':
    main()