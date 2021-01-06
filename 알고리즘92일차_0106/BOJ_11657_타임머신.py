import sys
input=sys.stdin.readline

def bel():
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    for _ in range(N-1):
        for i in range(1,N+1):
            for v2,val in arr[i]:
                if distance[v2] > distance[i]+val:
                    distance[v2] = distance[i]+val
    for i in range(1,N+1):
        for v2,val in arr[i]:
            if distance[v2] > distance[i] + val:
                return -1
    return distance
N,M =  map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    v1,v2,val = map(int,input().split())
    arr[v1] += [(v2,val)]

result = bel()

if result == -1:
    print(-1)
else:
    for i in range(1,len(result)):
        if result[i] == 'inf':
            print(-1)
        else:
            print(result[i])