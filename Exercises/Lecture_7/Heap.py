class MaxHeap:
    def __init__(self) -> None:
        self.h = [None]
        self.n = 0
    
    def less(self, x, y):
        return 1<=x<=self.n and 1<=y<=self.n and self.h[x]<self.h[y]
    
    def swap(self, x, y):
        temp = self.h[x]
        self.h[x] = self.h[y]
        self.h[y] = temp
    
    def parent(self, x):
        return x//2
    
    def left(self, x):
        return 2*x
    
    def right(self, x):
        return 2*x+1

    def bubbleUp(self, node):
        p = self.parent(node)
        if (self.less(p, node)):
            self.swap(node, p)
            self.bubbleUp(p)

    def bubbleDown(self, node):
        l = self.left(node)
        r = self.right(node)
        child = l + self.less(l, r)
        if (self.less(node, child)):
            self.swap(node, child)
            self.bubbleDown(child)
    
    def max(self):
        return self.h[1]
    
    def insert(self, x):
        self.h.append(x)
        self.n += 1
        self.bubbleUp(self.n)
    
    def extractMax(self):
        r = self.h[1]
        self.h[1] = self.h[self.n]
        self.h.pop()
        self.n -= 1
        self.bubbleDown(1)
        return r