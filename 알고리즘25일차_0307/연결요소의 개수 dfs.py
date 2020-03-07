import sys
sys.setrecursionlimit(10000)
def dfs(k,li):
    for i in range(1,N+1):
        if arr[k][i] == 1 and visit[i] == 0:
            visit[i] = 1
            li += [i]
            dfs(i,li)
N, M = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    r, c = map(int,input().split())
    arr[r][c] = arr[c][r] = 1
visit = [0] * (N+1)
result =  []
for z in range(1,N+1):
    li2 = []
    dfs(z,li2)
    if li2:
        result += [li2]
for t in range(1,N+1):
    if visit[t] == 0:
        result += [t]
print(len(result))