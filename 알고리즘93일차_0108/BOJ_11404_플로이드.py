import sys
input=sys.stdin.readline

N = int(input())
INF = float('inf')
arr = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    v1,v2,val = map(int,input().split())
    arr[v1][v2] = min(arr[v1][v2],val)
for z in range(1,N+1):
    arr[z][z] = 0
    for i in range(1,N+1):
        for j in range(1, N + 1):
            if arr[i][j] > arr[i][z] + arr[z][j]:
                arr[i][j] = arr[i][z] + arr[z][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == INF:
            print(0 ,end=" ")
        else:
            print(arr[i][j],end=" ")
    print()