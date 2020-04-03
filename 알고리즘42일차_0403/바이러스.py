def bfs(k):
    global q, arr, visit,count
    q += [k]
    visit[k] = 1
    while q:
        r = q.pop(0)
        for i in range(N+1):
            if arr[r][i] == 1 and visit[i] != 1:
                visit[i] = 1
                q += [i]
                count[i] = 1

N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1
visit = [0] * (N+1)
count = [0] * (N+1)
q = []
bfs(1)
print(sum(count))