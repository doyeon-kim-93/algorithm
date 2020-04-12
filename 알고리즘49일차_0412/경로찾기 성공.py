from collections import deque
def bfs(r,c):
    global q,result,flag,visit
    visit[r] = 1
    q += [(s,[s])]
    while q:
        point, li = q.popleft()
        if point != c:
            for x in range(N+1):
                if cmap[point][x] == 1 and visit[x] == 0:
                    visit[x] = 1
                    q += [(x,li+[x])]
        else:
            result += [[len(li),li]]

N,k = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
s,e = map(int,input().split())
cmap = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        con = 0
        for z in range(k):
            if arr[i][z] != arr[j][z]:
                con += 1
        if con == 1:
            cmap[i+1][j+1] = 1
visit = [0] *(N+1)
q = deque()
result = []
bfs(s,e)
if len(result) == 0:
    print(-1)
else:
    con = 987654321
    po = 0
    for i in range(len(result)):
        if result[i][0] < con:
            po = i
    print(*result[po][1])