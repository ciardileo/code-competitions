"""
Pessoa tem V valor
A = conta do açougue
F = conta da farmácia
P = conta da padaria
Descobrir o maior número de contas que ele consegue pagar
"""

""" 
Adicionar as contas em uma lista
Ordenar a lista em ordem crescente
Para cada item da lista:
    checar se consegue pagar ele
"""

def main():
    v = int(input())
    a = int(input())
    f = int(input())
    p = int(input())

    contas = [a, f, p]
    contas.sort() # complexidade O(n log n)
    n_contas = 0

    if v >= contas[0]:
        n_contas += 1
        if v >= contas[0] + contas[1]:
            n_contas += 1
            if v >= sum(contas):
                n_contas += 1
                
    print(n_contas)
    
if __name__ == "__main__":
    main()

