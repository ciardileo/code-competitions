"""
estrutura de dados stack/pilha
"""

name = input("Name: ")
print(name)

stack = [i for i in name]

for word in range(len(name)):  # complexidade linear: O(1) * len(name)
    last_word = stack.pop()
    print(last_word, end='')