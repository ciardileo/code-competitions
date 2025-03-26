"""
sequencia de 1 a N
achar numero de elementos da maior subsequencia que siga as regras
no maximo dois numeros diferentes, não podem ter dois numeros iguais consecutivos
https://neps.academy/br/exercise/467
"""

def main():
    N = int(input())
    
    sequence = list()
    numbers = set()
    
    def calculate(n1, n2):
        actual = list()
        actual.append(0)
        
        for i in range(len(sequence)):      
            if sequence[i] == n1 or sequence[i] == n2:
                if len(actual) == 1:
                    actual.append(sequence[i])
                elif sequence[i] != actual[-1]:
                    actual.append(sequence[i])
                    
        return len(actual) - 1
    
    for _ in range(N):
        number = int(input())
        sequence.append(number)
        numbers.add(number)
    
    numbers = list(numbers)
    result = 1
    for i in range(len(numbers)):
        for j in range(i + 1 , len(numbers)):
            result = max(result, calculate(numbers[i], numbers[j]))
    
    print(result)
        
        
    
    
if __name__ == '__main__':
    main()