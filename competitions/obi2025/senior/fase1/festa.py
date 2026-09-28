def main():
    E = int(input())
    S = int(input())
    L = int(input())
    
    if (S <= E and L <= E) or (S >= E and L >= E):
        resultado = max(abs(S - E), abs(L - E)) * 2
        print(resultado)
    else:
        resultado = abs(S - E) * 2 + abs(L - E) * 2
        print(resultado)    
    

if __name__ == "__main__":
    main()