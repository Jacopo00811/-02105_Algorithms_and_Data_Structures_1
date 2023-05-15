class WeightedUnion_extended:
    def __init__(self, N):
        self.sz = [1 for _ in range(N)]
        self.p = [i for i in range(N)]
    
    def find_pc(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_pc(self.p[x])
        return self.p[x]

    def connected(self, u, v):
        if self.find_pc(u) == self.find_pc(v):
            return True
        return False

    def union(self, i, j):
        r_i = self.find_pc(i)
        r_j = self.find_pc(j)
        if r_i != r_j:
            if self.sz[r_i] < self.sz[r_j]:
                self.p[r_i] = r_j
                self.sz[r_j] += self.sz[r_i]
            else:
                self.p[r_j] = r_i
                self.sz[r_i] += self.sz[r_j]

N, M = map(int, input().split())
Inputs = [input().split() for _ in range(M)]
Dynamic_connectivity = WeightedUnion_extended(N)

for line in Inputs:
    if line[0]=='A':
        Dynamic_connectivity.union(int(line[1]), int(line[2]))
    elif line[0]=='C':
        if Dynamic_connectivity.connected(int(line[1]), int(line[2])) == True:
            print("YES")
        else:
            print("NO")