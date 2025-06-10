"""
encontrar o maior subarray com o algoritmo de kadane
"""

def main():
    salas = int(input())
    corredor = [int(x) for x in input().split()]
    
    max_ending_here = corredor[0]
    max_so_far = corredor[0]
    
    for i in range(1, salas):
        max_ending_here = max(corredor[i], max_ending_here + corredor[i])
        max_so_far = max(max_so_far, max_ending_here)
        
    print(max_so_far)
    
    
if __name__ == "__main__":
    main()