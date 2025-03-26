from collections import defaultdict

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def is_connected(parent, x, y):
    return find(parent, x) == find(parent, y)

def max_passengers(N, B, boats, queries):
    boats.sort(key=lambda x: x[2], reverse=True)
    results = []

    for X, Y in queries:
        parent = list(range(N + 1))
        rank = [0] * (N + 1)

        max_capacity = 0
        for I, J, P in boats:
            union(parent, rank, I, J)
            if is_connected(parent, X, Y):
                max_capacity = P
                break

        results.append(max_capacity)

    return results

def main():
    N, B = map(int, input().split())

    boats = []
    for _ in range(B):
        I, J, P = map(int, input().split())
        boats.append((I, J, P))

    C = int(input())
    queries = []
    for _ in range(C):
        X, Y = map(int, input().split())
        queries.append((X, Y))

    results = max_passengers(N, B, boats, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
