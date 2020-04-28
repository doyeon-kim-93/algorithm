from collections import deque

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]
def bfs():
    global sand,q,pre_sand,H,W
    con = 1
    while q:
        r,c,z = q.popleft()
        if z != con:
            for a in range(H):
                for b in range(W):
                    if dist[a][b] == 1:
                        dist[a][b] = 0
                        sand -= arr[a][b]
                        arr[a][b] = '.'
            if pre_sand == sand:
                return con-1
            else:
                pre_sand = sand
                con = z
        cnt = 0
        for t in range(8):
            nr = r + dr[t]
            nc = c + dc[t]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] == '.':
                cnt += 1
        if arr[r][c] <= cnt:
            dist[r][c] = 1
        else:
            q += [(r,c,z+1)]

H,W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
dist = [[0]*W for _ in range(H)]
sand = 0
pre_sand = 0
q = deque([])
for i in range(H):
    for j in range(W):
        if arr[i][j] != '.' :
            arr[i][j] = int(arr[i][j])
            sand += arr[i][j]
            q += [(i,j,1)]
print(bfs())