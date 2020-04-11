from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs1():
    global q, q1, q2, landmap, landcolor,result,arr
    while q:
        r,c = q.popleft()
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<N:
                if landmap[nr][nc][0] == 0:
                    landmap[nr][nc][0] = 1
                    landmap[nr][nc][1] = landcolor
                    q1 += [(nr,nc)]
                    q2 += [(nr,nc)]
                elif arr[nr][nc] == 1:
                    q += [(nr,nc)]
                    arr[nr][nc] = 2
                    landmap[nr][nc][1] = landcolor

def chc():
    global q, q1, q2, landmap, landcolor,result,arr
    while q2:
        r, c = q2.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if landmap[nr][nc][0] == 1001 and landmap[nr][nc][1] != landmap[r][c][1] :
                    result = min(result, landmap[r][c][0])

def bfs2():
    global q, q1, q2, landmap, landcolor,result,arr
    while q1:
        r,c = q1.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<N:
                if landmap[nr][nc][0] == 0:
                    landmap[nr][nc][0] = landmap[r][c][0] + 1
                    landmap[nr][nc][1] = landmap[r][c][1]
                    q1 += [(nr,nc)]
                elif landmap[nr][nc][0] == 1001:
                    pass
                else:
                    if landmap[nr][nc][1] != landmap[r][c][1]:
                        bridge = landmap[nr][nc][0] + landmap[r][c][0]
                        result = min(result,bridge)

N = int(input())
landmap = [[[0] * 2 for _ in range(N)] for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            landmap[i][j][0] = 1001
q = deque([])
q1 = deque([])
q2 = deque([])
result = 987654321
landcolor = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            landcolor += 1
            arr[i][j] = 2
            landmap[i][j][1] = landcolor
            q += [(i,j)]
            bfs1()
chc()
if result == 1:
    print(result)
else:
    bfs2()
    print(result)