def plateau(A):
    max_length = 1
    current_length = 1
    for i in range(1, len(A) - 1):
        if A[i-1] < A[i] == A[i+1]:
            current_length += 1
        else:
            current_length = 1
        max_length = max(max_length, current_length)
    return max_length
