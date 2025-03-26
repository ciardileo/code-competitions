"""
cifra:
    cada consoante vira 3 letras:
     1.  ela mesma
     2.  vogal mais próxima, se houver duas escolher a mais próxima do inicio
     3. a próxima consoante, se for z é ele mesmo
     
https://neps.academy/br/exercise/1487
"""

def main():
    alpha = 'abcdefghijklmnopqrstuvxz'
    vogals = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvxz'
    
    alpha_dict = {}
    for i, letra in enumerate(alpha):
        alpha_dict[letra] = i
    
    def consoante(letter: str, index):
        new = letter
        l_index = index
        count = -1
        loop = 1
        while True:
            if loop % 2 != 0:
                if l_index + count >= 0:
                    if alpha[l_index + count] in vogals:
                        new = new + alpha[l_index + count]
                        break
            else:
                if l_index - count <= 23:
                    if alpha[l_index - count] in vogals:
                        new = new + alpha[l_index - count]
                        break
            
                count -= 1
                    
            loop += 1
            
        if letter != 'z':
            while True:
                l_index += 1
                if alpha[l_index] in consonants:
                    new = new + alpha[l_index]
                    return new
        
        return new + 'z'
        
    
    word = input()
    
    result = ''
    for letter in word:
        if letter in consonants:
            result += consoante(letter, alpha_dict[letter])
        else:
            result += letter
        
    print(result)
    
    
    
if __name__ == "__main__":
    main()