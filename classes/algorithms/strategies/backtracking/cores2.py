"""
criar um algoritmo que calcule a possibilidade de organização de 4 cores em uma linha, sendo que Azul não pode ficar com Vermelho

primeiro ponto: ser capaz de construir um algoritmo de "backtracking" que faz todas as possibilidades
"""

def main():
    cores = ["Azul", "Vermelho", "Amarelo", "Verde"]
    def backtracking(actual_sequence: list = []):
        if len(actual_sequence) == 4:
            return 1
        
        count = 0
        
        for i in range(len(cores)):
            if cores[i] not in actual_sequence:
                if actual_sequence:
                    if (actual_sequence[-1] == "Azul" and cores[i] == "Vermelho") or (actual_sequence[-1] == "Vermelho" and cores[i] == "Azul"):
                        continue
                    
                actual_sequence.append(cores[i])
                count += backtracking(actual_sequence)
                actual_sequence.pop()
        
            
        return count
    
    print(backtracking())
        
if __name__ == "__main__":
    main()