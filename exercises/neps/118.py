def main():
    risada = input()
    vogais = set(("a", "e", "i", "o", "u"))
    risada_vogais = []
    
    for letra in risada:
        if letra in vogais:
            risada_vogais.append(letra)

    if risada_vogais == list(reversed(risada_vogais)):
        print("S")
    else:
        print("N")
    
    
    
    
if __name__ == "__main__":
    main()