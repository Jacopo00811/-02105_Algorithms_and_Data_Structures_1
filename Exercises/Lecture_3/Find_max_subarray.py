
def find_max_subarray(A):
    n = len(A)
    max_sum = float('-inf')
    start_index = end_index = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(A[i:j+1])
            if max_sum < current_sum:
                max_sum = current_sum
                start_index = i 
                end_index = j
    return A[start_index:end_index+1]


print(find_max_subarray([1, -2, 3, 4, -5, 6, 7, -8, 9, -10]))