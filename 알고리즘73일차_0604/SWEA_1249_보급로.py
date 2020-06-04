import sys
sys.stdin = open("input.txt", "r")

import collections
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    global q
    while q:
        r,c = q.popleft()
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<N:
                if visit[nr][nc] == -1:
                    visit[nr][nc] = visit[r][c]+arr[nr][nc]
                    q += [(nr,nc)]
                else:
                    if visit[nr][nc] > visit[r][c]+arr[nr][nc]:
                        visit[nr][nc] = visit[r][c] + arr[nr][nc]
                        q += [(nr,nc)]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visit = [[-1]*N for _ in range(N)]
    q = collections.deque([])
    q += [(0,0)]
    visit[0][0] = 0
    bfs()
    print('#{} {}'.format(tc,visit[N-1][N-1]))