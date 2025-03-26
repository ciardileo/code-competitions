"""
cada lance é composto pelo nome e valor oferecido
"""

def main():
    n = int(input())
    lances = []

    for _ in range(n): # complexidade de O(n)
        nome = input()
        valor = int(input())
        lances.append([nome, valor])
        
    maior = 0 
    for lance in range(1, len(lances)): # complexidade de O(n)
        if lances[lance][1] > lances[maior][1]:
            maior = lance
            
    print(lances[maior][0])
    print(lances[maior][1])
        
if __name__ == "__main__":
    main()