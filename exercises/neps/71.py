"""
encontrar quantas formas de fazer o saque com as notas existem
"""

def main():
    saque = int(input())
    qtd_notas = [int(x) for x in input().split()]
    notas = [2, 5, 10, 20, 50, 100]
    
    def backtrack(nota_atual=0, soma_atual=0, actual_sequence=[]):
        if soma_atual == saque:
            print(actual_sequence)
            return 1
        
        count = 0
        
        for i in range(nota_atual, len(notas)):
            if soma_atual + notas[i] > saque and soma_atual != saque:
                return 0
            
            if qtd_notas[i] > 0:
                qtd_notas[i] -= 1
                actual_sequence.append(notas[i])
                count += backtrack(nota_atual, soma_atual + notas[i], actual_sequence)
                qtd_notas[i] += 1
                actual_sequence.pop()
            else:
                nota_atual = i + 1
            
                
        return count
    
    
    print(backtrack())
                
                
    
    
    

if __name__ == "__main__":
    main()