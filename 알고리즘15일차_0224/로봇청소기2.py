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
    cnt = 1
    board[r][c] = 2
    while 1 :
        flag = False
        for i in range(4):
            di = turn(d)
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<M and 0<=nc<N and board[nr][nc] == 0:
                cnt += 1
                board[nr][nc] = 2
                r = nr
                c = nc
                d = di
                flag = True
                break
        if not flag:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            elif d == 3:
                c += 1
            if board[r][c] == 1:
                break
            else:
                clean()
    return print(cnt)

N, M = map(int,input().split())
r, c, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
clean(r,c,d)
