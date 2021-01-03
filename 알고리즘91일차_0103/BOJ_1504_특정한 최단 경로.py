import sys
input=sys.stdin.readline
import heapq

def disk(s,e):
    distance = [float('inf')]*(N+1)
    distance[s] = 0
    q = []
    heapq.heappush(q,[distance[s],s])
    while q:
        dis,current_node = heapq.heappop(q)
        if distance[current_node] < dis:
            continue
        for v2,val in arr[current_node]:
            dist = dis + val
            if dist < distance[v2]:
                distance[v2] = dist
                heapq.heappush(q,[distance[v2],v2])
    return distance[e]

N,E = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(E):
    v1,v2,val = map(int,input().split())
    arr[v1] += [(v2,val)]
    arr[v2] += [(v1,val)]
v3,v4 = map(int,input().split())

result_s1 = disk(1,v3)
result_m1 = disk(v3,v4)
result_e1 = disk(v4,N)

result_s2 = disk(1,v4)
result_m2 = disk(v4,v3)
result_e2 = disk(v3,N)

result1 = result_e1+result_m1+result_s1
result2 = result_e2+result_m2+result_s2

if result1 == float('inf') and result2 == float('inf'):
    print(-1)
else:
    print(min(result1,result2))

