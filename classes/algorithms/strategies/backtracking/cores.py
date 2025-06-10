"""
algoritmo para encontrar o número de combinações para por 4 blocos coloridos em uma fila, de forma que Azul e Vermelho não fiquem juntos
"""

def backtrack(pieces, sequence, used, all_combinations):
    # Se a sequência tem o tamanho correto, adicionamos às combinações válidas
    if len(sequence) == len(pieces):
        all_combinations.append(list(sequence))
        return
    
    # Tenta adicionar cada peça que ainda não foi usada
    for i in range(len(pieces)):
        if not used[i]:
            # Checa a restrição antes de adicionar
            if sequence and ((sequence[-1] == "Azul" and pieces[i] == "Vermelha") or 
                             (sequence[-1] == "Vermelha" and pieces[i] == "Azul")):
                continue
            
            # Marca a peça como usada e adiciona à sequência
            used[i] = True
            sequence.append(pieces[i])
            
            # Continua a construção da sequência
            backtrack(pieces, sequence, used, all_combinations)
            
            # Remove a peça e a desmarca (backtracking)
            sequence.pop()
            used[i] = False

def find_valid_combinations(pieces):
    all_combinations = []
    used = [False] * len(pieces)
    backtrack(pieces, [], used, all_combinations)
    return all_combinations

def main():
    pieces = ["Azul", "Vermelha", "Verde", "Amarela"]
    valid_combinations = find_valid_combinations(pieces)
    
    # Exibe todas as combinações válidas
    for combination in valid_combinations:
        print(combination)

if __name__ == "__main__":
    main()