"""
saber se é possível levar as caixas para cima
já vi a resolução desse exercício, então só vou tentar passar pro papel a lógica da ordem para subir tudo
dica: sempre analisar bem, porque todo exercício tem um algoritmo implícito para resolver o problema

1. sobe a prinmeira, desce nada;
2. sobe a segunda, desce a primeira;
3. sobe a terceira, desce a segunda;
4. sobe a segunda

"""

def main():
    n_caixas = int(input())
    caixas = [int(x) for x in input().split()]
    
    # verificando se é possível subir:
    caixas.sort()
    
    if caixas[0] > 8:
        print("N")
        return
    
    for i in range(1, len(caixas)):
        if caixas[i] - caixas[i-1] > 8:
            print("N")
            return
    
    print("S")
    
    # criando o algoritmo para saber os passos
            
    

if __name__ == "__main__":
    main()