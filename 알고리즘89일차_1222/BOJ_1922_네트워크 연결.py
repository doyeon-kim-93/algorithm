# N = int(input())
# M = int(input())
# G = [[] for _ in range(N+1)]
# for i in range(M):
#     v1, v2, val = map(int,input().split())
#     G[v1] += [(v2,val)]
#     G[v2] += [(v1,val)]
# INF = 987654321
# visit = [0] * (N+1)
# parent = [None] * (N+1)
# distance = [INF]*(N+1)
#
# def prim(s):
#     distance[s] = 0
#     for _ in range(N):
#         idx = -1
#         min = INF
#         for i in range(1,N+1):
#             if not visit[i] and distance[i] < min:
#                 idx = i
#                 min = distance[i]
#         visit[idx] = 1
#         for v,val in G[idx]:
#             if not visit[v] and val < distance[v]:
#                 distance[v] = val
#                 parent[v] = idx
# prim(1)
# print(distance)
# print(sum(distance[1:]))

import heapq

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2, val = map(int,input().split())
    G[v1] += [(val,v2)]
    G[v2] += [(val,v1)]
visit = [0] * (N+1)
distance = [0]*(N+1)
q = []
for i in G[1]:
    heapq.heappush(q,i)
visit[1] = 1
def prim(s):
    while q:
        val,v2 = heapq.heappop(q)
        if not visit[v2]:
            visit[v2] = 1
            distance[v2] = val
            for j in G[v2]:
                heapq.heappush(q,j)
        if sum(visit) == N:
            return

prim(1)
print(sum(distance[1:]))