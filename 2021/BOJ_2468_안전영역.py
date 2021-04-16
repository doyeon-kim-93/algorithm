dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check(k):
    global N,arr,result
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= k:
                visit[i][j] = 1
    val = 0
    q = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                val += 1
                q += [(i,j)]
                visit[i][j] = 1
                while q:
                    r,c, = q.pop(0)
                    for z in range(4):
                        nr = r + dr[z]
                        nc = c + dc[z]
                        if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            q += [(nr,nc)]
    result = max(result,val)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxVal = 0
for i in range(N):
    for j in range(N):
        maxVal = max(maxVal,arr[i][j])
result = -1
for i in range(0,maxVal+1):
    check(i)
print(result)