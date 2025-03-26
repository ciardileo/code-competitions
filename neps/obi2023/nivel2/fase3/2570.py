"""
formar uma pirâmide em que cada andar tenha o mesmo peso

o topo da pirâmide sempre será pesos[0]

para testar o segundo andar e depois o terceiro, fazemos um backtracking
"""

def main():
    pesos = [int(x) for x in input().split()]
    pesos.sort(reverse=True)
    
    topo = pesos[0]
    
    for i in range(1, 6):
        for j in range(i + 1, 6):
            if pesos[i] + pesos[j] == topo:
                
                soma = 0
                for k in range(1, 6):
                    if k != i and k != j:
                        soma += pesos[k]
                        
                if soma == topo:
                    print("S")
                    return
                
    print("N")
    

if __name__ == "__main__":
    main()