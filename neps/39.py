import sys
sys.setrecursionlimit(10 ** 8)

def main():
    N, K = [int(x) for x in input().split()]
    
    def backtrack(count=0, actual_sequence=[]):
        # Caso base: se a sequência atual tiver tamanho N, verificamos se é válida
        if len(actual_sequence) == N:
            if count >= K:  # Se tiver exatamente K bits consecutivos, é inválida
                return 0
            return 1  # Sequência válida
        
        result = 0
        
        # Tentar adicionar os dois possíveis bits (0 ou 1)
        for i in range(2):
            # Se estamos adicionando um '1', incrementamos o contador de bits consecutivos
            if i == 1:
                if count + 1 < K:  # Podemos adicionar mais um '1' sem quebrar a regra
                    result += backtrack(count + 1, actual_sequence + [i])
            else:
                # Se estamos adicionando um '0', resetamos o contador de bits consecutivos
                result += backtrack(0, actual_sequence + [i])
        
        return result
    
    print(backtrack())
    
if __name__ == "__main__":
    main()
