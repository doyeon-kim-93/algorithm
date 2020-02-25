dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
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
    global cnt
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    di = turn(d)
    nr = r + dr[di]
    nc = c + dc[di]
    if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0:
        clean(nr,nc,di)
    else:
        if d == 0:
            if board[r+1][c] == 1 :
                return
            else:
                clean(r+1,c,d)
        elif d == 1:
            if board[r][c-1] == 1:
                return
            else:
                clean(r,c-1,d)
        elif d == 2:
            if board[r-1][c] == 1:
                return
            else:
                clean(r-1,c,d)
        elif d == 3:
            if board[r][c+1] == 1:
                return
            else:
                clean(r,c+1,d)
N, M = map(int,input().split())
r, c, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
clean(r,c,d)
print(cnt)