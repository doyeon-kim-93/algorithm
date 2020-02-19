# import sys
# sys.setrecursionlimit(100000)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(r,c):
    for x in range(4):
        nr = r + dr[x]
        nc = c + dc[x]
        if 0<= r <= N-1 and 0<= c <= M-1:
            if arr[r][c] == 1:
                arr[r][c] = 5
                dfs(nr,nc)

T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]

    cnt = 0
    for i in range(k):
        c,r =map(int,input().split())
        arr[r][c] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i,j)

