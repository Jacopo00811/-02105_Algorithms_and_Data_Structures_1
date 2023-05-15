n = int(input())
numbers = list(map(int, input().split()))

def best_mid(left, mid, right):
	sum = numbers[mid]
	best_left = sum

	for i in range(mid - 1, left - 1, -1):
		sum += numbers[i]
		best_left = max(best_left, sum)
	
	sum = numbers[mid + 1]
	best_right = sum

	for i in range(mid + 2, right + 1):
		sum += numbers[i]
		best_right = max(best_right, sum)
	
	return best_left + best_right

def best(left, right):
	if left == right:
		return numbers[left]

	mid = (left + right) // 2

	left_max = best(left, mid)
	right_max = best(mid + 1, right)
	mid_max = best_mid(left, mid, right)

	return max([left_max, right_max, mid_max])

print(best(0, n-1))