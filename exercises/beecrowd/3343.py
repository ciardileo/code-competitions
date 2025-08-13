"""
se a muralha for maior ou igual ao titã, destrói K metros da muralha e morre
se a muralha for menor que o titã, ele pula e segue para a próxima
"""

def main():
    n, x = [int(x) for x in input().split()]  # número de titãs, tamanho das muralhas
    titas = input()
    p, m, g = [int(x) for x in input().split()]  # tamanho dos titas
    muralhas_restantes = [0]
    total_muralhas = 0
    
    for tita in titas:
        hp = 0
        if tita == "P":
            hp = p
        elif tita == "M":
            hp = m
        else:
            hp = g
            
        if hp > max(muralhas_restantes):
            total_muralhas += 1
            if x - hp > 0:
                muralhas_restantes.append(x-hp)
                
        else:
            for i in range(len(muralhas_restantes)):
                if muralhas_restantes[i] >= hp:
                    muralhas_restantes[i] -= hp
                    break
                
    print(total_muralhas)
        
    
    
if __name__ == "__main__":
    main()