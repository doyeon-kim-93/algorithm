dr = [1,-1,0,0]
dc = [0,0,1,-1]
def turn(dir):
    if dir == 0:
        return 3
    elif dir == 1:
        return 0
    elif dir == 2:
        return 1
    elif dir == 3:
        return 2

def clean(r,c,d):
    if board[r][c] == 0:
        board[r][c] = 2
    if d == 0:
        if 0<=c-1<M:
            if board[r][c-1] == 0:
                clean(r,c-1,turn(d))
            else:
                clean(r,c,turn(d))
    elif d == 1:
        if 0<=r-1<N:
            if board[r-1][c] == 0:
                clean(r-1,c,turn(d))
            else:
                clean(r,c,turn(d))
    elif d == 2:
        if 0<=c+1<N:
            if board[r][c+1] == 0:
                clean(r,c+1,turn(d))
            else:
                clean(r,c,turn(d))
    elif d == 3:
        if 0<=r+1<N:
            if board[r+1][c] == 0:
                clean(r+1,c,turn(d))
            else:
                clean(r,c,turn(d))

def check(r,c,d):
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M:
            if board[nr][nc] == 1 or board[nr][nc] == 2:
                cnt += 1
    if cnt == 4:
        if dir == 0:
            if 0<=r+1<N:
                if board[r+1][c] != 0:
                    return
                else:
                    clean(r+1,c,d)
        elif dir == 1:
            if 0<=c-1<N:
                if board[r][c-1] != 0:
                    return
                else:
                    clean(r,c-1,d)
        elif dir == 2:
            if 0<=r-1<N:
                if board[r-1][c] != 0:
                    return
                else:
                    clean(r-1,c,d)
        elif dir == 3:
            if 0<=c+1<N:
                if board[r][c+1] != 0:
                    return
                else:
                    clean(r,c+1,d)

N, M = map(int,input().split())
r, c, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
result = 0
check(r,c,d)
for i in range(M):
    for j in range(N):
        if board[i][j] > 1:
            result += 1
print(result)