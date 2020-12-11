from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def move(r,c,z):
    cnt = 0
    while board[r+dr[z]][c+dc[z]] != '#' and board[r][c] != 'O':
        r += dr[z]
        c += dc[z]
        cnt += 1
    return r, c, cnt

def bfs():
    global q
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            r_x,r_y,r_cnt = move(rx,ry,i)
            b_x,b_y,b_cnt = move(bx,by,i)
            if board[b_x][b_y] == 'O':
                continue
            if board[r_x][r_y] == 'O':
                print(cnt)
                return
            if r_x == b_x and r_y == b_y :
                if r_cnt > b_cnt:
                    r_x -= dr[i]
                    r_y -= dc[i]
                else:
                    b_x -= dr[i]
                    b_y -= dc[i]
            if not visit[r_x][r_y][b_x][b_y]:
                visit[r_x][r_y][b_x][b_y] = 1
                q += [(r_x,r_y,b_x,b_y,cnt+1)]
    print(-1)

N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = deque([])
rx,ry,bx,by = 0,0,0,0
check = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i,j
        elif board[i][j] == 'B':
            bx, by = i,j

q.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = 1
bfs()