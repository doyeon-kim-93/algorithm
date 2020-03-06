dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(r,c):
    q.append((r,c))
    visit[r][c] = 1
    che[r][c] = 1
    while q :
        flag = False
        n, m = q.pop(0)
        for i in range(4):
            nr = n + dr[i]
            nc = m + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    che[nr][nc] = che[n][m] + 1
                    q.append((nr,nc))
                elif arr[nr][nc] == 2:
                    visit[nr][nc] = 1
                    che[nr][nc] = che[n][m] + 1
                    flag = True
                    break
        if flag:
            break
N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
arr[N-1][M-1] = 2
visit = [[0] * M for _ in range(N)]
che = [[0]*M for _ in range(N)]
q = []
bfs(0,0)
print(che[N-1][M-1])