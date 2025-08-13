# union-find
def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parents[y] = x
    elif rank[y] > rank[x]:
        parents[x] = y
    else:
        parents[x] = y
        rank[y] += 1

def main():
    global parents
    global rank
    N, M = map(int, input().split())  # número de alunos, número de linhas na lista
    parents = [i for i in range(N)]
    rank = [0 for i in range(N)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        union(x - 1, y - 1)
        
    count = 0
    for i in range(N):
        if i == parents[i]:
            count += 1
            
    print(count)
    
    
if __name__ == "__main__":
    main()# union-find
def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parents[y] = x
    elif rank[y] > rank[x]:
        parents[x] = y
    else:
        parents[x] = y
        rank[y] += 1

def main():
    global parents
    global rank
    N, M = map(int, input().split())  # número de alunos, número de linhas na lista
    parents = [i for i in range(N)]
    rank = [0 for i in range(N)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        union(x - 1, y - 1)
        
    count = 0
    for i in range(N):
        if i == parents[i]:
            count += 1
            
    print(count)
    
    
if __name__ == "__main__":
    main()