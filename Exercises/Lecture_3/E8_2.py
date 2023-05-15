n = int(input())
A = list(map(int, input().split()))

best = A[0]

for i in range(n):
	sum = 0
	for j in range(i, n):
		sum += A[j]
		if sum > best:
			best = sum
print(best)
