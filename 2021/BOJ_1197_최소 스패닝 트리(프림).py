import heapq

def prim(k):
    global q,result
    start = k
    while q:
        val,v = heapq.heappop(q)
        if not visit[v]:
            visit[v] = True
            distance[v] = val
            result += val
            for i in G[v]:
                heapq.heappush(q,i)
            parent[v] = start
            start = v

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
result = 0
G = [[] for _ in range(N)]
for ar in arr:
    v1,v2,w = ar
    G[v1-1] += [(w,v2-1)]
    G[v2-1] += [(w,v1-1)]

distance = [0]*N
visit = [0]*N
parent = [None]*N
q = []
for val,i in G[0]:
    heapq.heappush(q,(val,i))
visit[0] = 1
prim(0)
print(result)
