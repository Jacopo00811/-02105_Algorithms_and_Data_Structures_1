from heapq import heappush, heappop
N, M = map(int, input().split())

adj_list = [[] for i in range (N+1)]
for i in range (M):
    u,v,w = map(int, input ().split())
    adj_list[u].append((v, w)) 
    adj_list[v].append ((u, w))

distance = [None]*(N+1)
pq = [(-5, 1)]
while pq:
    dist, vertex = heappop(pq) 
    if distance[vertex] is None:
        distance[vertex] = dist # type: ignore
        for u, w in adj_list[vertex]:
            heappush(pq, (dist+w+5, u))
print(0, *distance[2:])