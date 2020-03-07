from collections import deque

def bfs(n,m):
    global q
    q += [n]
    while q:
        t = q.popleft()
        for i in range(N):
            if arr[t][i] == 1 and visit[i] == 0 :
                if i == m:
                    result[n][m] = 1
                else:
                    visit[i] = 1
                    q += [i]
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]
q = deque([])
for i in range(N):
    for j in range(N):
        visit = [0]*N
        bfs(i,j)
for x in range(N):
    print(' '.join(map(str,result[x])))