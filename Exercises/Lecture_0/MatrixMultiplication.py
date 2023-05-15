def MatrixMultiplication(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
"""
The function first initializes an n x n matrix C with zeros. It then performs matrix multiplication by iterating 
over the rows i of A, the columns j of B, and the intermediate index k. At each iteration, the product of the elements
at A[i][k] and B[k][j] is accumulated into C[i][j]. The result C is then returned.
"""