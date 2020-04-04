from collections import deque
dr = [1,-1,0,0]
dc = [0,0,-1,1]
def bfs(r,c,v):
    global q, visit, arr, result
    visit[r][c] = 1
    q.append([r,c,v])
    while q :
        a,b,c = q.popleft()
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0:
                if arr[nr][nc] == 'L':
                    visit[nr][nc] = 1
                    result = max(result,c+1)
                    q.append([nr,nc,c+1])

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
result = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visit = [[0]*M for _ in range(N)]
            q = deque([])
            bfs(i,j,0)
print(result)