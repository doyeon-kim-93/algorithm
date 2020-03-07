from collections import deque
def bfs(k,li):
    global q, result
    q += [k]
    while q:
        t = q.popleft()
        for j in range(1,N+1):
            if arr[t][j] == 1 and visit[j] == 0 and j not in li:
                visit[j] = 1
                q += [j]
                li += [j]
    if li:
        result += [li]
N, M = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    r, c = map(int,input().split())
    arr[r][c] = arr[c][r] = 1
visit = [0] * (N+1)
q = deque([])
result =  []
for z in range(1,N+1):
    bfs(z,[])
for t in range(1,N+1):
    if visit[t] == 0:
        result += [t]
print(len(result))
