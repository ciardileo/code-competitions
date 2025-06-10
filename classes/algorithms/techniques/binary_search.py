"""

"""

def main():
    N, M = [int(x) for x in input().split()]
    
    array = [int(x) for x in input().split()]
    array.sort()
    
    queries = [int(x) for x in input().split()]
    
    # for num in queries, verify if exists in array in a efficient method
    
    def binary_search(value):
        start = 0
        end = len(array) - 1
        
        while start <= end:
            middle = (start + end) // 2
            if array[middle] < value:
                start = middle + 1
            elif array[middle] > value:
                end = middle - 1
            else:
                return middle  # Valor encontrado
        
        return -1  # Valor não encontrado

        
    for i in queries:
        print(binary_search(i))

if __name__ == '__main__':
    main()