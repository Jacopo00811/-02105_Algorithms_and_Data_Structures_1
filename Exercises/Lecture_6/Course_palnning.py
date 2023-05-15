N, M = map(int, input().split(" "))

in_degree = [0 for _ in range(N+1)]
adj_list = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split(" "))
    adj_list[y].append(x)
    in_degree[x] += 1

current_semster = [y for y in range(1, N+1) if in_degree[y] == 0] # Add to the current semester only the courses
# with in-deg = 0
next_semster = []
count_semster = 0

while len(current_semster) != 0:
    for y in current_semster:
        for x in adj_list[y]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                next_semster.append(x)
    current_semster = next_semster
    next_semster = []
    count_semster += 1

print(count_semster)