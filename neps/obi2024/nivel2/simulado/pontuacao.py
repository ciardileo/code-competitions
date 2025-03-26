"""
Esportes: 2
Artes: 3
Ciências: 5
soma >= 200 = ouro O
150 <= nota < 200 = prata P
100 <= nota < 150 = bronze B
N
"""

def calculate_award(pontuation):
    if pontuation >= 200:
        return 'O'
    elif 150 <= pontuation < 200:
        return 'S'
    elif 100 <= pontuation < 150:
        return 'B'
    return 'N'

sports = int(input())
arts = int(input())
science = int(input())

pontuation = sports * 2 + arts * 3 + science * 5
print(calculate_award(pontuation))

