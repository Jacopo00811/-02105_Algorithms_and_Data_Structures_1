"""
In the following code, the priority queue q contains pairs of the form (d, x),
meaning that the current distance to node x is d. The list distance contains the
distance to each node, and the list processed indicates whether a node has been
processed. Initially the distance is 0 to x and ∞ to all other nodes.

"""
import heapq

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for i in range (M):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

def Dijkstra(adj, x, N):
    processed = [False]*(N+1)
    distance = [float('inf')]*(N+1)
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
        
    return distance[1:]

for i in Dijkstra(adj, 1, N):
    print(i, end =" ")