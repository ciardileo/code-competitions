"""

"""

def main():
    N = int(input())
    
    graph = {
        0: {2, 1},
        1: {2, 3},
        2: {3, 4},
        3: {4, 0},
        4: {1, 0}
    }
    
    dario, xerxes = 0, 0
    
    for _ in range(N):
        d, x = [int(x) for x in input().split()]  # 3, 1
        
        if d in graph[x]:
            xerxes += 1
        else:
            dario += 1
            
    if dario > xerxes:
        print('dario')
    else:
        print('xerxes')
            
    
    
if __name__ == "__main__":
    main()