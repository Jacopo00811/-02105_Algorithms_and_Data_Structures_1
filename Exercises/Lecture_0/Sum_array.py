def f(A):
    x = 0
    for i in range(len(A)):
        x+=A[i]
    return x

print(f([1,2,3]))