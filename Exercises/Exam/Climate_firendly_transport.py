import heapq

N, M, F = map(int, input().split())
adj = [[] for _ in range(N)] # N stations, 1 to N
planes_route = []

for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

for _ in range(F):
    x = list(map(int, input().split()))
    planes_route.append(x)


def Dijkstra(adj, x, N):
    processed = [False]*(N)
    distance = [float('inf')]*(N)
    distance[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while (len(q) > 0):
        d, a = heapq.heappop(q)
        if (processed[a]):
            continue
        processed[a] = True
        for (b, w) in adj[a]:
            if (distance[a] + w < distance[b]):
                distance[b] = distance[a] + w
                heapq.heappush(q, (distance[b], b))
    return distance

for i in range(len(planes_route)):
    x = planes_route[i]
    a = x[0]
    b = x[1]
    list = Dijkstra(adj, a, N)
    if list[planes_route[i][1]] > 120:
        print("keep")
    else:
        print("cancel")
