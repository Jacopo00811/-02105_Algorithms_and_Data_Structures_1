class WeightedUnion_extended:
    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.initial_stone = N*M
        self.final_stone = N*M+1
        self.totalSize = N*M+2
        self.sz = [1 for _ in range(self.totalSize)]
        self.p = [i for i in range(self.totalSize)]
        self.removed =  [False for _ in range(self.totalSize)]
        self.removed[self.initial_stone] = True
        self.removed[self.final_stone] = True
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def connected(self, u, v):
        if self.find(u) == self.find(v):
            return True
        return False

    def unionIfPossible(self, i, j):

        if self.removed[j]:
            r_i = self.find(i)
            r_j = self.find(j)
            if r_i != r_j:
                if self.sz[r_i] < self.sz[r_j]:
                    self.p[r_i] = r_j
                    self.sz[r_j] += self.sz[r_i]
                else:
                    self.p[r_j] = r_i
                    self.sz[r_i] += self.sz[r_j]
    
    def connectToAdjacent(self, i):
        if i < self.N:
            # print("Connecting initial stone")
            self.unionIfPossible(i, self.initial_stone)
        elif i >= (self.N*(self.M - 1)):
            # print("Connecting final stone")
            self.unionIfPossible(i, self.final_stone)

        self.removed[i] = True

        j = i-1
        # if (j >= 0 and j < M*N):
        if (j // self.N == i // self.N):
            self.unionIfPossible(i, j)

        j = i+1
        # if (j >= 0 and j < M*N):
        if (j // self.N == i // self.N):
            self.unionIfPossible(i, j)
        
        j = i-self.N
        if (j >= 0 and j < M*N):
            self.unionIfPossible(i, j)
        
        j = i+self.N
        if (j >= 0 and j < M*N):
            self.unionIfPossible(i, j)

    def connectetStartAndEnd(self):
        
        # self.printSet()
        if self.connected(self.initial_stone, self.final_stone):
            return True
        return False
    
    def printSet(self):
        print("___\nSet:")
        for i in range(0, len(self.p), N):
            line = [f"{x:5}" for x in self.p[i:i+self.N]]
            print(" ".join(line))
        print("___")


N = int(input())
M = int(input())
R = int(input())

tuples_list = [tuple(map(int, input().split())) for _ in range(R)]
Weighted_Union = WeightedUnion_extended(M, N)

minTime = 0
for line in tuples_list:
    minTime += 1
    pos = line[1] * N + line[0]
    Weighted_Union.connectToAdjacent(pos)
    if Weighted_Union.connectetStartAndEnd():
        print(minTime)
        break
