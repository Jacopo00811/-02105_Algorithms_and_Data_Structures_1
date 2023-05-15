class WeightedUnion:
    def __init__(self, N):
        self.sz = [1 for _ in range(N)]
        self.p = [i for i in range(N)]
    
    def find_pc(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_pc(self.p[x])
        return self.p[x]

    
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


N = int(input())
M = int(input())
Inputs = [input().split() for _ in range(M)]
Weighted_Union = WeightedUnion(N)

for line in Inputs:
    if line[0]=='F':
        print(Weighted_Union.find_pc(int(line[1])))
    elif line[0]=='U':
        Weighted_Union.union(int(line[1]), int(line[2]))