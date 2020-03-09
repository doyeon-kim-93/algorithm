from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(a,b,con):
    global q ,result
    arr[a][b] = con
    result[con] += 1
    q += [(a,b)]
    while q :
        r, c = q.popleft()
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0 <= nr < M and 0<= nc < N :
                if arr[nr][nc] == -2:
                    arr[nr][nc] = con
                    result[con] += 1
                    q += [(nr,nc)]
M, N, K = map(int,input().split())
arr = [[-2] * N for _ in range(M)]
q = deque([])
result = []
for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    i1 = M-y2
    i2 = M-y2 + abs(y2-y1)
    j1 = x1
    j2 = x1 + abs(x2-x1)
    for i in range(i1,i2):
        for j in range(j1,j2):
            arr[i][j] = -1
con = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == -2:
            result += [0]
            bfs(i,j,con)
            con += 1
result.sort()
print(len(result))
print(' '.join(map(str,result)))
