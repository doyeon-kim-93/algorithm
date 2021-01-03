import sys
input=sys.stdin.readline
import heapq

def disk(ar,s):
    distance = [float('inf') for _ in  range(N+1)]
    distance[s] = 0
    q = []
    heapq.heappush(q,[distance[s],s])

    while q:
        current_distance, current_node = heapq.heappop(q)
        if distance[current_node] < current_distance:
            continue
        for v2,val in ar[current_node]:
            dis = (current_distance + val)
            if dis < distance[v2]:
                distance[v2] = dis
                heapq.heappush(q,[dis,v2])
    return distance

N,M,end = map(int,input().split())
arr = [[] for _ in range(N+1)]
r_arr = [[] for _ in range(N+1)]
for _ in range(M):
    v1,v2,val = map(int,input().split())
    arr[v1] += [(v2,val)]
    r_arr[v2] += [(v1,val)]
Toend = disk(arr,end)
Tohome = disk(r_arr,end)
result = [0]*(N+1)
for i in range(N+1):
    result[i] = (Toend[i]+Tohome[i])
print(max(result[1:]))