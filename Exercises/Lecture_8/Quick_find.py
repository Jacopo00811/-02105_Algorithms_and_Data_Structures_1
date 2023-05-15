class QuickFind:
    def __init__(self, N):
        self.id = [i for i in range(N)]
        self.size = N
    
    def find(self, i):
        return self.id[i]

    def union(self, i, j):
        iID = self.find(i)
        jID = self.find(j)
        if iID != jID:
            for k in range(self.size):
                if self.id[k] == iID:
                    self.id[k] = jID

N = int(input())
M = int(input())
Inputs = [input().split() for _ in range(M)]
Quick_Find = QuickFind(N)

for line in Inputs:
    if line[0]=='F':
        print(Quick_Find.find(int(line[1])))
    elif line[0]=='U':
        Quick_Find.union(int(line[1]), int(line[2]))