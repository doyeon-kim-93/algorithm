from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    global q, result,flag
    while q:
        r,c,v = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if v == 1 and arr[nr][nc] == '.' and visit[nr][nc][v] == 0:
                    visit[nr][nc][1] = 1
                    q += [(nr,nc,1)]
                elif v == 0 and arr[nr][nc] == '.'and visit[nr][nc][1] == 0 and visit[nr][nc][0] == 0:
                    visit[nr][nc][0] = visit[r][c][0] + 1
                    q += [(nr,nc,0)]
                    if nr == 0 or nr == N-1 or nc == 0 or nc == M-1:
                        result = min(result,visit[nr][nc][0])
                        flag =True
T = int(input())
for tc in range(T):
    M,N = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    q = deque([])
    flag2 = False
    result = 987654321
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                q.appendleft((i,j,1))
                visit[i][j][1] = 1
            elif arr[i][j] == '@':
                q += [(i,j,0)]
                visit[i][j][0] = 1
                if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                    result = 1
                    flag2 = True
    flag = False
    if flag2:
        print(result)
    else:
        bfs()
        if flag:
            print(result)
        else:
            print('IMPOSSIBLE')