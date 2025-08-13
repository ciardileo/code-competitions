"""
a mensagem só pode ser dos aliens se, e somente se, todos os caracteres forem do alfabeto
basta passar por todos os caracteres da mensagem e verificar se eles são do alfabeto
"""


def main():
    K, N = map(int, input().split())  # caracteres do alfabeto alienigena, caracteres da mensagem
    alfabeto_alien = input()
    mensagem = input()
    
    for char in mensagem:
        if char not in alfabeto_alien:
            print("N")
            return False
        
    print("S")
    
    
if __name__ == "__main__":
    main()