dr = [0,-1,0,1]
dc = [-1,0,1,0]

drr = [0,0,1,-1]
dcc = [1,-1,0,0]

br = [1,0,-1,0]
bc = [0,-1,0,1]
def check():
    global result,visit,q,arr,N,M
    while q:
        r,c,v = q.pop(0)
        cnt = 0
        for i in range(4):
            nr = r + drr[i]
            nc = c + dcc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc] == 1 or arr[nr][nc] == 1:
                    cnt += 1
        if cnt == 4:
            nr = r + br[v]
            nc = c + bc[v]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1:
                    break
                else:
                    q += [[nr,nc,v]]
        else:
            nr = r + dr[v]
            nc = c + dc[v]
            if 0<=nr<N and 0<=nc<M:
                if visit[nr][nc] == 0 and arr[nr][nc] == 0:
                        visit[nr][nc] = 1
                        result +=1
                        nv = (v+3)%4
                        q += [[nr,nc,nv]]
                elif visit[nr][nc] == 1 or arr[nr][nc] == 1:
                    nv = (v + 3) % 4
                    q += [[r,c,nv]]

N,M = map(int,input().split())
r,c,v = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
result = 1
q = [[r,c,v]]
visit[r][c] = 1
check()
print(result)