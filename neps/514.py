"""

"""

def main():
    valores = [int(x) for x in input().split()]
    
    cormengo = 3 * valores[0] + valores[1]
    flaminthia = 3 * valores[3] + valores[4]
    
    if cormengo > flaminthia:
        print("C")
    elif cormengo < flaminthia:
        print("F")
    else:
        if valores[2] > valores[5]:
            print("C")
        elif valores[2] < valores[5]:
            print("F")
        else:
            print("=")
            

if __name__ == "__main__":
    main()