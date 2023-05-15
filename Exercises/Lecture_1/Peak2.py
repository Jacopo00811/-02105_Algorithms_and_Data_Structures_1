n = int(input()) 
A = list(map(int, input().split()))
max = 0 

def Peak2(A, n):
    max = 0
    for i in range(n):
        if A[i] > A[max]:
            max = i
    return max

