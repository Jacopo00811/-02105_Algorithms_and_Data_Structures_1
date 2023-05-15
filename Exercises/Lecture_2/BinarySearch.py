def BinarySearch(A, i, j, x):
    if j < i:
        return False
   
    m = (i+j)//2

    if A[m] == x: 
        return True
    elif A[m] < x:
        return BinarySearch(A, m+1, j, x)
    else: 
        return BinarySearch(A, i, m-1, x)