dr = [1,-1,0,0]
dc = [0,0,-1,1]

updr = [0,-1,0,1]
updc = [1,0,-1,0]

downdr = [0,1,0,-1]
downdc = [1,0,-1,0]

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
air = []
for i in range(N):
    if arr[i][0] == -1:
        air += [(i,0)]
    if len(air) == 2:
        break
while T:
    T -= 1
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                val = arr[i][j]
                spread = val//5
                cnt = 0
                for z in range(4):
                    nr = i + dr[z]
                    nc = j + dc[z]
                    if 0<=nr<N and 0<=nc<M and arr[nr][nc] != -1:
                        cnt += 1
                        tmp[nr][nc] += spread
                tmp[i][j] += val -(cnt*spread)
            elif arr[i][j] == -1:
                tmp[i][j] = -1
    arr = [tmp[i][:] for i in range(N)]
    for i in range(2):
        if i == 0:
            dir = 0
            r,c = air[i][0],air[i][1]+1
            arr[r][c] = 0
            while 1:
                if arr[r][c] == -1:
                    break
                if (r == air[i][0] and c == M-1) or (r == 0 and c == M-1) or (r == 0 and c == 0):
                    dir += 1
                nr = r + updr[dir]
                nc = c + updc[dir]
                if 0<=nr<N and 0<=nc<M:
                    if arr[nr][nc] != -1:
                        arr[nr][nc] = tmp[r][c]
                    r, c = nr, nc
        else:
            dir = 0
            r,c = air[i][0],air[i][1]+1
            arr[r][c] = 0
            while 1:
                if arr[r][c] == -1:
                    break
                if (r == air[i][0] and c == M-1) or (r == N-1 and c == M-1) or (r == N-1 and c == 0):
                    dir += 1
                nr = r + downdr[dir]
                nc = c + downdc[dir]
                if 0<=nr<N and 0<=nc<M:
                    if arr[nr][nc] != -1:
                        arr[nr][nc] = tmp[r][c]
                    r, c = nr, nc
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != -1:
            result += arr[i][j]
print(result)

