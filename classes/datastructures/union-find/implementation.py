class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]  # N = qtd de elementos
        self.qtd = [1 for _ in range(N)]
        self.rank = [0 for _ in range(N)]
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        self.parents[x] = self.find(x)
        return self.parents[x]
    
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return 
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
            self.qtd[root_x] += self.qtd[root_y]
        elif self.rank[root_y] > self.rank[root_x]:
            self.parents[root_x] = root_y
            self.qtd[root_y] += self.qtd[root_x]
        else:
            self.parents[root_x] = root_y
            self.rank[root_y] += 1;
            self.qtd[root_y] += self.qtd[root_x]
    