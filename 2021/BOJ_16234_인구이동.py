dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check(i,j,visit):
    q = [(i,j)]
    visit[i][j] = 1
    tmp = [(i,j)]
    val = arr[i][j]
    while q:
        r,c = q.pop(0)
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                    visit[nr][nc] = 1
                    q += [(nr,nc)]
                    tmp += [(nr, nc)]
                    val += arr[nr][nc]
    # print(val)
    # print(tmp)
    # print(visit)
    value = val//len(tmp)
    for r,c in tmp:
        arr[r][c] = value

N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
while 1:
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                for z in range(4):
                    nr = i + dr[z]
                    nc = j + dc[z]
                    if 0<=nr<N and 0<=nc<N:
                        if L <= abs(arr[i][j]-arr[nr][nc]) <= R:
                            cnt += 1
                            check(i,j,visit)
                            break
    if cnt:
        result += 1
    else:
        break
print(result)
