dr = [0,0,-1,1]
dc = [1,-1,0,0]

def check(r,c,visit):
    if visit[r][c] == 1:
        return False
    q = [(r,c)]
    visit[r][c] = 1
    while q:
        y,x = q.pop(0)
        for z in range(4):
            nr = y + dr[z]
            nc = x + dc[z]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and arr[nr][nc] > 0:
                visit[nr][nc] = 1
                q += [(nr,nc)]
    return True

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            ice += [(i,j,arr[i][j])]
        if (i == 0 and j == 0) or (i == N-1 and j == M-1):
            arr[i][j] = 0
flag = True
result = 0
while ice:
    result += 1
    tmp = [[0]*M for _ in range(N)]
    q = ice[:]
    tmpIce = []
    while q:
        r,c,val = q.pop(0)
        cnt = 0
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 0:
                    cnt += 1
        newVal = val - cnt
        if newVal > 0:
            tmpIce += [(r,c,newVal)]
            tmp[r][c] = newVal
    ice = tmpIce[:]
    arr = [tmp[i][:] for i in range(N)]
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    for r,c,val in ice:
        if check(r,c,visit):
            cnt += 1
    if cnt > 1:
        flag = False
        break
if flag:
    print(0)
else:
    print(result)

for val in arr:
    print(val)


