def MergeSort(A, i, j):
    if i < j:
        m =(i+j)//2
        MergeSort(A, i, m)
        MergeSort(A, m+1, j)
        Merge(A, i, m, j)

def Merge(A, i, m, j):
    Left = A[i:m+1]
    Right = A[m+1:j+1]
    Left.append(float('inf'))
    Right.append(float('inf'))
    x = y = 0
    for k in range(i, j+1):
        if Left[x] <= Right[y]:
            A[k] = Left[x]
            x += 1
        else:
            A[k] = Right[y]
            y += 1