"""
10 tons diferentes
numerados de 0 a 9
os quadrados não numerados serão pintados com o número da cor da distância dele para um quadrado 0
"""

def colorir(quadrado, cores):
    for i in range(len(cores['-1'])):
        minimo = abs(cores['-1'][i] - cores['0'][0])
        
        for j in range(1, len(cores['0'])):
            if abs(cores['-1'][i] - cores['0'][j]) > minimo:
                quadrado[cores['-1'][i]] = minimo
                break
            else:
                minimo = abs(cores['-1'][i] - cores['0'][j])
            
        if quadrado[cores['-1'][i]] == -1:
            quadrado[cores['-1'][i]] = minimo if minimo <= 9 else 9
    
    return quadrado
            

n = int(input())

quadrado = [int(x) for x in input().split()]

cores = {
    '-1': [x for x in range(len(quadrado)) if quadrado[x] == -1],
    '0': [x for x in range(len(quadrado)) if quadrado[x] == -0],
}

print(*colorir(quadrado, cores), sep=' ')
