from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check():
    global visit,q
    while q:
        r,c = q.popleft()
        for s in range(4):
            nr = r + dr[s]
            nc = c + dc[s]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == -1:
                visit[nr][nc] = visit[r][c] + 1
                q.append((nr, nc))

T = int(input())
for tc in range(1,T+1):
    q = deque()
    N,M = map(int,input().split())
    visit = [[-1] * M for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(M):
            if tmp[j]=='W':
                q.append((i, j))
                visit[i][j] = 0
    check()
    result = 0
    for i in range(N):
        for j in range(M):
            result += visit[i][j]
    print('#{} {}'.format(tc,result))