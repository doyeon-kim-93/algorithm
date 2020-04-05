from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
N,M = map(int,input().split())
def bfs(a,b):
    global visit,arr,result,flag,q
    visit[a][b] = 1
    q += [(a,b)]
    while q :
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    q += [(nr,nc)]
                if nr == N-1 and nc == M-1:
                    visit[nr][nc] = visit[r][c] + 1
                    flag = True
    if flag:
        result = max(result,visit[N-1][M-1])

arr = [list(map(int,input())) for _ in range(N)]
q = deque([])
result = 0
flag = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 :
            arr[i][j] = 0
            visit = [[0]*M for _ in range(N)]
            bfs(0,0)
            arr[i][j] = 1
if flag:
    print(result)
else:
    print(-1)