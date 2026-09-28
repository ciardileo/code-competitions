"""
A: volume mínimo de leite
B: volume máximo de leite
C: capacidade da xícara
D: quantidade da dose de espresso
"""

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    # lógica: vamos considerar a quantidade de leite restante como C - A (pra vermos o número máximo de espressos)
    # 1: se não der pra colocar nenhum espresso, já deu erro
    # 2: tenta colocar o máximo de espresso que der
    # 3: se o que sobrar adicionado a A exceder B, então não serve também
    
    restante = C - A
    
    if (restante < D):
        print("N")
    else:
        restante = restante % D
        
        if (A + restante) > B:
            print("N")
        else:
            print("S")    

if __name__ == "__main__":
    main()