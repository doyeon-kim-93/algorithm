import sys
sys.stdin = open("input.txt", "r")

import heapq
from sys import stdin
input = stdin.readline

INF = float('inf')
def dijsk():
    global start,N,arr
    q = []
    visit = [INF] * (N+1)
    visit[start] = 0
    heapq.heappush(q,[0,start])

    while q :
        cost, city = heapq.heappop(q)
        if visit[city]<cost:
          continue
        for endCity,costValue in arr[city]:
            costValue += cost
            if costValue < visit[endCity]:
                visit[endCity] = costValue
                heapq.heappush(q,[costValue,endCity])
    return visit

N,M = map(int,input().split())
start = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    i,j,v = map(int,input().split())
    arr[i] += [(j,v)]
result = dijsk()
for i in range(1,len(result)):
    if result[i] == INF:
        print('INF')
    else:
        print(result[i])