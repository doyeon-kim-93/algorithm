from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(a,b,d):
    global q
    visit[a][b] = 1
    q += [(a,b)]
    while q :
        r, c = q.popleft()
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0 <= nr < N and 0<= nc < N :
                if city[nr][nc] > d and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    q += [(nr,nc)]
def check(k):
    global M
    M = max(int(k),M)
    return int(k)

M = -1
N = int(input())
city = [list(map(check,input().split())) for _ in range(N)]
q = deque([])
result = -1
for t in range(M+1):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if city[x][y] > t and visit[x][y] == 0:
                bfs(x,y,t)
                cnt += 1
    result = max(result,cnt)
print(result)