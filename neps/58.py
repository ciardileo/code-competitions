"""
determinar quantas seções vão ser cobertas por agua
uma seção pode ser considerada coberta se ela possuir água com pelo menos 1m de profundidade
"""

def main():
    secoes = int(input())
    alturas = []
    
    for _ in range(secoes):
        alturas.append(int(input()))
        
    corte = max(alturas)
    
    
    
    for i in range(secoes):
        if i == 0:
            pass 
    

if __name__ == "__main__":
    main()