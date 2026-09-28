"""
fazer um sistema de compressão RLE
numero de vezes - caracter repetido

para cada letra em sequence, iniciar uma sequencia caso não esteja em uma, se o caracter atual não for igual ao anterior e estivermos em uma sequência, o contador para e é retornado o count 
https://neps.academy/br/exercise/2435
"""

def main():
    N = int(input())
    sequence = input()
    result = ""
    
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            count += 1
        else:
            result += f"{count} {sequence[i-1]} "
            count = 1    
            
    result += f"{count} {sequence[-1]}"

        
    print(result)

if __name__ == "__main__":
    main()