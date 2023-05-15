i=0
j = int(input())
A = list(map(int, input().split()))
res = 0
while (i<=j):
    m = (i+j)// 2
    if (m == j-1 or A[m] >= A[m+1]) and A[m] >= A[m-1]:
        res = m 
    elif A[m-1] > A[m]:
        j = m-1
    elif A[m] < A[m+1]: 
        j = m+1
