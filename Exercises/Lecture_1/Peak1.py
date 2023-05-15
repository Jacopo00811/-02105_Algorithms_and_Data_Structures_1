n = int(input()) 
A = list(map(int, input().split()))
res = 0

def Peak1(A, n):
    if A[0] >= A[1]:
        return 0
    for i in range(1, n-2):
        if A[i-1] <= A[i] and A[i] >= A[i+1]:
            return i
    if A[n-2] <= A[n-1]:
        return n-1
