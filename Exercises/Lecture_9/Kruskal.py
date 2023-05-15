class UnionFind:
    def __init__(self, N):     
        self.sz = [1 for _ in range(N)]
        self.p = [i for i in range(N)]
            
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x] 
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
        
    def union(self, i, j):
        r_i = self.find(i)
        r_j = self.find(j)
        if self.sz[r_i] > self.sz[r_j]:
            self.p[r_j] = r_i
            self.sz[r_i] += self.sz[r_j]
        else:
            self.p[r_i] = r_j
            self.sz[r_j] += self.sz[r_i]


N, M = map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(M)]


def Kruskal(edges):
    # Sort edges according to their weight
    edges.sort(key=lambda edge:edge[2])
    counter = 0
    MST_weight = 0
    # Create a new union find structure with N+1 vertices
    # because they start counting from node 1
    U = UnionFind(N+1)
    # Loops through edges in sorted order
    for i in range(len(edges)):
        u, v, w = edges[i]
        # Edges are not connected = do not create a cycle in the tree
        if not U.connected(u, v):
            # Add edge u to v to the tree
            U.union(u, v)
            counter += 1
            # Increase the total weight of tree
            MST_weight += w

    return MST_weight

print(Kruskal(edges))