"""
estrategia gulosa
"""

def main():
    valor = int(input())
    moedas = [100, 50, 25, 10, 5, 1]
    n_moedas = 0

    for moeda in moedas:
        # print(f"Moeda de {moeda}:")
        while valor >= moeda:
            # print(f"{valor} - {moeda}, +1 moeda ({n_moedas + 1})")
            valor -= moeda
            n_moedas += 1
            
    print(n_moedas)
        
    
if __name__ == "__main__":
    main()