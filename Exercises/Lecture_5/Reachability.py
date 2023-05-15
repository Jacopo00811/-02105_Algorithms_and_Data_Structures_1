n, m, a, b = [int(i) for i in input().split()]
n = n+1 
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    x, y = [int(i) for i in input().split()]
    adjacency_list[x].append(y)
    adjacency_list[y].append(x)

def DFS(adjacency_list, a, b):
    stack = []
    visited = [False]*n
    # visited = [False for _ in range(n)]
    stack.append(a)
    visited[a] = True

    while stack: # Means "while stack is not empty"
        current = stack.pop()
        for v in adjacency_list[current]:
            if v == b:
                return True
            if not visited[v]:
                stack.append(v)
                visited[v] = True
    return False

if DFS(adjacency_list, a, b):
    print("YES")
else:
    print("NO")
    