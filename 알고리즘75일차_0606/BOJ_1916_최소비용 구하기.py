import heapq
from sys import stdin
input = stdin.readline

INF = float('inf')
def dijsk():
    global start,end,N,arr
    q = []
    visit = [INF] * (N+1)
    visit[start] = 0
    heapq.heappush(q,[start,0])

    while q :
        city , cost = heapq.heappop(q)
        if visit[city]<cost:
          continue
        for endCity,costValue in arr[city]:
            costValue += cost
            if costValue < visit[endCity]:
                visit[endCity] = costValue
                heapq.heappush(q,[endCity,costValue])
    return visit[end]

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    i,j,v = map(int,input().split())
    arr[i] += [(j,v)]
start,end = map(int,input().split())

print(dijsk())