from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[[0]*4 for _ in range(m)] for _ in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

def bfs():
    q = deque()
    q.append((sx-1, sy-1, sd-1))
    while q:
        x, y, d = q.popleft()
        if x == ex-1 and y == ey-1 and d == ed-1:
            print(dist[x][y][d])
            return
        for i in range(1, 4):
            nx, ny = x+dx[d]*i, y+dy[d]*i
            if 0<=nx<n and 0<=ny<m :
                if a[nx][ny]:
                    break
                if not dist[nx][ny][d]:
                    q.append((nx, ny, d))
                    dist[nx][ny][d] = dist[x][y][d]+1
        for i in range(4):
            if i == d:
                continue
            k = 1
            if (i+d)%4 == 1:
                k = 2
            if not dist[x][y][i]:
                q.append((x, y, i))
                dist[x][y][i] = dist[x][y][d]+k

bfs()