import sys,copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    global q,two_result,w,cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q += [(nx, ny)]
                    cnt += 1
def con(k,start):
    global add_three, three,zero_list
    if k == 3:
        a = copy.deepcopy(three)
        add_three += [a]
    else:
        for i in range(start,len(zero_list)):
            three += [zero_list[i]]
            con(k+1,i+1)
            three.pop()
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
wall_cnt = 3
zero_list = []
two = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            wall_cnt += 1
        elif arr[i][j] == 0:
            zero_list += [(i,j)]
        else:
            two += 1
ready_result = N*M - wall_cnt
add_three = []
three = []
con(0,0)
q = deque([])
two_result = 987654321
for z in range(len(add_three)):
    w = copy.deepcopy(arr)
    for k in range(3):
        a,b = add_three[z][k]
        w[a][b] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2:
                q += [(i, j)]
    bfs()
    two_result = min(two_result,(two+cnt))
print(ready_result-two_result)
