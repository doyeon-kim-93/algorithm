import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline
from collections import deque
INF = float('inf')

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    visit = [[INF]*M for _ in range(N)]
    q  = deque([])
    q.append((0,0))
    visit[0][0] = 0
    while q:
        r,c = q.popleft()
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<M:
                if visit[nr][nc]>visit[r][c] + arr[nr][nc]:
                    visit[nr][nc] = visit[r][c] + arr[nr][nc]
                    q += [(nr,nc)]
    return visit[N-1][M-1]
M,N = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]
print(bfs())
