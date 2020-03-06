dr = [1,-1,0,0]
dc =[0,0,1,-1]
def bfs(k):
    global result
    while k:
        r, c = k.pop(0)
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 0 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    arr[nr][nc] = 1
                    con[nr][nc] = con[r][c] + 1
                    result = con[nr][nc]
                    k.append((nr,nc))
M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
con = [[0]*M for _ in range(N)]
q= []
result = 0
flag = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 :
            flag = False
        elif arr[i][j] == 1:
            visit[i][j] = 1
            q.append((i,j))
if flag:
    print(0)
else:
    bfs(q)
    flag2 = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                print(-1)
                flag2 = False
                break
    if flag2:
        print(result)