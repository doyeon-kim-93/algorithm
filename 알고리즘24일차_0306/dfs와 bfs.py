def dfs(k,visit):
    for i in range(1,n+1):
        if arr[k][i] == 1 and i not in visit:
            visit.append(i)
            dfs(i,visit)
    return visit
def bfs(k):
    visited[k] = 1
    result.append(k)
    q.append(s)
    while q:
        h =q.pop(0)
        for i in range(n+1):
            if arr[h][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                result.append(i)

n, m, s = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    y, x = map(int,input().split())
    arr[y][x] = 1
    arr[x][y] = 1
q = []
result = []
visited = [0] * (n+1)
bfs(s)
print(' '.join(map(str,dfs(s,[s]))))
print(' '.join(map(str,result)))

