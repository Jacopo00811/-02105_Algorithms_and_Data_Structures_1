def FindMax(A, n):
    max = 0
    for i in range(n):
        if A[i] > max:
            max = A[i]
    return max