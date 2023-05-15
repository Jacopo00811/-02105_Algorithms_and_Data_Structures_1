class QuickUnion:
    def __init__(self, N):
        self.p = [i for i in range(N)]
    
    def find(self, i):
        while i != self.p[i]:
            i = self.p[i]
        return i

    def union(self, i, j):
        r_i = self.find(i)
        r_j = self.find(j)
        if r_i != r_j:
            self.p[r_i] = r_j

N = int(input())
M = int(input())
Inputs = [input().split() for _ in range(M)]
Quick_Union = QuickUnion(N)

for line in Inputs:
    if line[0]=='F':
        print(Quick_Union.find(int(line[1])))
    elif line[0]=='U':
        Quick_Union.union(int(line[1]), int(line[2]))