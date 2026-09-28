"""
analisar cada palavra de uma string
dada uma lista de letras, ver quantas palavras da string possuem pelo menos uma das letras da lista
"""

def result(text_words, letters):
    count = 0
    for word in text_words:
        for letter in letters:
            if letter in word:
                count += 1 
                break
                
    return count
    
text_words = input().split()
letters = input()

print(result(text_words, letters))
