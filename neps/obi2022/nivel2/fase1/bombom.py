"""
A J Q K nos 4 naipes C E O P
Naipe dominante é o da carta virada no começo
Se o naipe for dominante, a carta vale 4 pontos a mais
https://neps.academy/br/exercise/2070
"""

def main():
    values = {
        'A': 10,
        'J': 11, 
        'Q': 12,
        'K': 13
    }
    
    dominant = input()[1]  
    
    luana = []
    for _ in range(3):
        luana.append(input())
        
    edu = []
    for _ in range(3):
        edu.append(input())
        
    def pontuation(deck):
        total = 0
        for card in deck:
            points = 0 if card[1] != dominant else 4
            points += values[card[0]]
            total += points
            
        return total
    
    points_luana = pontuation(luana)
    points_edu = pontuation(edu)
    
    if points_luana > points_edu:
        print("Luana")
    elif points_luana == points_edu:
        print('empate')
    else:
        print("Edu")
                
    
    
if __name__ == "__main__":
    main()