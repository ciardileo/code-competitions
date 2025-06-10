"""

"""

def main():
    N = int(input())
    numeros = []
    
    for _ in range(N):
       numero = int(input())
       
       if numero == 0:
           numeros.pop() 
           continue
       
       numeros.append(numero)
    
    print(sum(numeros))
    
    
if __name__ == "__main__":
    main()