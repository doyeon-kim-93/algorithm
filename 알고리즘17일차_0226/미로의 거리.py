dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(sr,sc):
    global result
    Q.append((sr,sc))
    maze[sr][sc] = '.'
    while Q :
        r , c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < N and 0<= nc < N and maze[nr][nc] != 1 and maze[nr][nc] != '.':
                Q.append((nr,nc))
                cnt[nr][nc] = cnt[r][c] + 1
                if maze[nr][nc] == 3:
                    result = cnt[nr][nc]-1
                    return
                maze[nr][nc] = '.'
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    cnt = [[0]*N for _ in range(N)]
    visit = []
    Q = []
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                bfs(i,j)
    print('#{} {}'.format(tc, result))