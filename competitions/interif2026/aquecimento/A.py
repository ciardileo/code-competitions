"""
frascos 0 1 2
conta as vogais e vê o resto da divisão por 3
"""

def main():
    palavra = input().lower()
    vogais = set(("a", "e", "i", "o", "u"))
    n_vogais = 0
    
    for letra in palavra:
        if letra in vogais:
            n_vogais += 1
            
    resultado = n_vogais % 3
    
    print(f"frasco {resultado}")
    
    
if __name__ == "__main__":
    main()