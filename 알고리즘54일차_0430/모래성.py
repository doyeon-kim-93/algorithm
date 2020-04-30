from collections import deque

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]
def bfs():
    global q
    con = 1
    while q:
        r,c,z = q.popleft()
        if z != con:
            con = z
        for t in range(8):
            nr = r + dr[t]
            nc = c + dc[t]
            if 0<=nr<H and 0<=nc<W and arr[nr][nc] != '.':
                arr[nr][nc] -= 1
                if arr[nr][nc] <= 0:
                    arr[nr][nc] = '.'
                    q += [(nr,nc,z+1)]

    return con-1
H,W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
q = deque([])
for i in range(H):
    for j in range(W):
        if arr[i][j] != '.' :
            arr[i][j] = int(arr[i][j])
        else:
            q += [(i,j,1)]
print(bfs())