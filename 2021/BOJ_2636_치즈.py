dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(air,arr):
    q2 = air[:]
    visit = [[0]*M for _ in range(N)]
    for r,c in q2:
        visit[r][c] = 1
        arr[r][c] = -1
    while q2:
        r,c = q2.pop(0)
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] == 0:
                visit[nr][nc] = 1
                arr[nr][nc] = -1
                q2 += [(nr,nc)]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q += [(i,j)]
check([(0,0)],arr)
result = 0
valList = [len(q)]
while q:
    result += 1
    tmpq = q[:]
    tmp = [arr[i][:] for i in range(N)]
    saveList = []
    newair = []
    while tmpq:
        r,c = tmpq.pop(0)
        con = 4
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == -1:
               con -= 1
        if con == 4:
            saveList += [(r,c)]
            tmp[r][c] = 1
        else:
            newair += [(r,c)]
    check(newair,tmp)
    valList += [len(saveList)]
    q = saveList[:]
    arr = [tmp[i][:] for i in range(N)]

print(result)
print(valList[-2])