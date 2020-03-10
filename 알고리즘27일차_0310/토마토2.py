from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
dh = [1,-1]
def bfs(day,high,y,x):
    global q ,green_tomato,result
    while q :
        d,h,r,c = q.popleft()
        if result < d :
            result += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<M and 0<=nc<N and box[h][nr][nc] == 0:
                box[h][nr][nc] = 1
                green_tomato -= 1
                q += [(d+1,h,nr,nc)]
        for z in range(2):
            nh = h + dh[z]
            if 0<= nh < H and box[nh][r][c] == 0:
                box[nh][r][c] = 1
                green_tomato -= 1
                q += [(d+1,nh,r,c)]
def check(k):
    global green_tomato
    if int(k) == 0:
        green_tomato += 1
    return int(k)
N, M, H = map(int,input().split())
box = []
green_tomato = 0
result = 0
for i in range(H):
    box += [[]]
    box[i] = [list(map(check,input().split())) for _ in range(M)]
if green_tomato == 0:
    print(0)
else:
    q = deque([])
    for z in range(H):
        for i in range(M):
            for j in range(N):
                if box[z][i][j] == 1:
                    q += [(0,z,i,j)]
    bfs(*q[0])
    if green_tomato == 0:
        print(result)
    else:
        print(-1)