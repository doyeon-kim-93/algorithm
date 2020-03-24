import sys
sys.setrecursionlimit(100000)
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def dfs(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc] == 0:
                arr[nr][nc] = -1
                dfs(nr,nc)
            elif arr[nr][nc] == 1:
                arr[nr][nc] = 2
def reset():
    global cnt,chz
    con = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 0
                con += 1
                chz -= 1
    cnt = con
def chz_cnt(k):
    global chz
    if int(k) == 1:
        chz += 1
    return int(k)
N, M = map(int,input().split())
chz = 0
arr = [list(map(chz_cnt,input().split())) for _ in range(N)]
cnt = 0
time = 0
while chz :
    time += 1
    dfs(0,0)
    reset()
print(time)
print(cnt)