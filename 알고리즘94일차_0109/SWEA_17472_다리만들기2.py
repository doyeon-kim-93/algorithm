import sys
import collections
import heapq
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def isl_check(x,y,z):
    q = collections.deque([])
    q += [(x,y)]
    visit[x][y] = 1
    arr[x][y] = z
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] == 1:
                visit[nr][nc] = 1
                arr[nr][nc] = z
                q += [(nr,nc)]

def distance_update(r,c,idx):
    global distance
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            x,y = nr,nc
            num = 1
            while 1:
                x += dr[i]
                y += dc[i]
                if 0 <= x < N and 0 <= y < M and arr[x][y] == 0:
                    num += 1
                elif 0 <= x < N and 0 <= y < M and arr[x][y] != 0:
                    if num != 1:
                        distance[arr[r][c]][arr[x][y]] = min(distance[arr[r][c]][arr[x][y]],num)
                    break
                elif 0 > x  or x >= N or 0 > y or y >= M:
                    break
                elif arr[x][y] == idx:
                    break

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1,v2):
    r1 = find(v1)
    r2 = find(v2)

    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += 1

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
cnt = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visit[i][j] == 0:
            isl_check(i,j,cnt)
            cnt += 1

distance = [[float('inf')]*(cnt) for _ in range(cnt)]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            distance_update(i, j,arr[i][j])

# edges = []
# for i in range(1,cnt):
#     for j in range(1,cnt):
#         if distance[i][j] != float('inf') and distance[i][j] != 1:
#             heapq.heappush(edges,(distance[i][j],i,j))

edges = []
for i in range(1,cnt):
    for j in range(1,cnt):
        if distance[i][j] != float('inf') and distance[i][j] != 1:
            edges += [(distance[i][j],i,j)]

edges.sort(key=lambda x:x[0])
result = []
answer = 0

parent = dict()
rank = dict()

for i in range(1,cnt):
    make_set(i)

for edge in edges:
    w,v1,v2 = edge
    if find(v1) != find(v2):
        union(v1,v2)
        result += [edge]
        answer += edge[0]

check = find(1)
for i in range(1,cnt):
    if find(i) != check:
        answer = -1
        break
print(answer)