import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline
from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    global result,flag,waterQ
    while kosumQ:
        for _ in range(len(waterQ)):
            r, c = waterQ.popleft()
            for z in range(4):
                nr = r + dr[z]
                nc = c + dc[z]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '.'and arr[nr][nc] != 'D':
                    arr[nr][nc] = '*'
                    visit[nr][nc] = 2
                    water[nr][nc] = 1
                    waterQ.append((nr, nc))
        flag2 = False
        for _ in range(len(kosumQ)):
            flag3 = False
            y,x,cnt = kosumQ.popleft()
            for z in range(4):
                ny = y + dr[z]
                nx = x + dc[z]
                fakecnt = cnt
                if 0<=ny<N and 0<=nx<M:
                    if arr[ny][nx] == '.' and visit[ny][nx] == 0 and water[ny][nx] == 0:
                        fakecnt += 1
                        kosumQ.append((ny,nx,fakecnt))
                        visit[ny][nx] = 1
                    elif arr[ny][nx] == 'D':
                        cnt += 1
                        flag2 = True
                        flag = True
                        flag3 = True
                        result = min(result,cnt)
                        break
            if flag3:
                break
        if flag2:
            break
N,M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
water = [[0]*M for _ in range(N)]
waterQ = deque([])
kosumQ = deque([])

for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            waterQ.append((i,j))
            visit[i][j] = 2
            water[i][j] = 1
        elif arr[i][j] == 'S':
            kosumQ.append((i,j,0))
            visit[i][j] = 1
        elif arr[i][j] == 'X':
            visit[i][j] = 1
result = 987654321
flag = False
bfs()
if flag:
    print(result)
else:
    print('KAKTUS')
