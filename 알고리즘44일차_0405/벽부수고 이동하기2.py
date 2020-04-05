from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
N,M = map(int,input().split())
def bfs(a,b,c):
    global visit,arr,result,flag,q
    visit[a][b][c] = 1
    q += [(a,b,c)]
    while q :
        r,c,v = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M :
                if arr[nr][nc] == 0 and visit[nr][nc][v] == -1:
                    visit[nr][nc][v] = visit[r][c][v] + 1
                    q += [(nr,nc,v)]
                if v == 0 and arr[nr][nc] == 1 and visit[nr][nc][v+1] == -1:
                    visit[nr][nc][v+1] = visit[nr][nc][v] + 1
                    q += [(nr,nc,v+1)]
arr = [list(map(int,input())) for _ in range(N)]
visit = [[[-1]*2 for _ in range(M)] for _ in range(N)]
q = deque([])
bfs(0,0,0)

if visit[N-1][M-1][0] == -1 :
    print(visit[N-1][M-1][1])
elif visit[N-1][M-1][1] == -1 :
    print(visit[N-1][M-1][0])
else:
    print(min(visit[N-1][M-1]))