import math

def Peak3(A, i, j):
    m = (i+j)// 2
    if (m == j-1 or A[m] >= A[m+1]) and A[m] >= A[m-1]:
        return m 
    elif A[m-1] > A[m]:
        return Peak3(A, i , m-1)
    elif A[m] < A[m+1]: 
        return Peak3(A, m+1, j)



j = int(input())
A = list(map(int, input().split()))
print(Peak3(A, 0, j))