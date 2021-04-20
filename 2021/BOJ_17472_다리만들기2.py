dr = [-1,1,0,0]
dc = [0,0,-1,1]

#섬 번호 붙이기
def island(r,c,visit,num):
    global arr,N,M
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] == 1:
            visit[nr][nc] = 1
            arr[nr][nc] = num
            island(nr,nc,visit,num)

#섬별로 거리 연결하기
def iDistance(r,c,n):
    global distances,N,M
    for z in range(4):
        cnt = 0
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
            cnt += 1
            while 1:
                nr += dr[z]
                nc += dc[z]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 0:
                        cnt += 1
                    elif arr[nr][nc] != n and arr[nr][nc] != 0 and cnt != 1:
                        distances[n-1][arr[nr][nc]-1] = min(distances[n-1][arr[nr][nc]-1], cnt)
                        break
                    elif arr[nr][nc] != n and arr[nr][nc] != 0 and cnt == 1:
                        break
                    elif arr[nr][nc] == n:
                        break
                else:
                    break
#조합으로 찾기
def check(cnt,island,cost,visit):
    global num,result,distances
    # print(visit,cnt,island,cost)
    if cnt >= num:
        result = min(result,cost)
    for i in range(num):
        if distances[island][i] != -1 and visit[i] == 0 and distances[island][i] != 987654321:
            visit[i] = 1
            check(cnt+1,i,cost+distances[island][i],visit)
            check(cnt + 1, island, cost + distances[island][i],visit)
            visit[i] = 0

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
islandVisit = [[0]*M for _ in range(N)]
num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and islandVisit[i][j] == 0:
            num += 1
            arr[i][j] = num
            islandVisit[i][j] = 1
            island(i,j,islandVisit,num)
distances = [[987654321]*num for _ in range(num)]
for z in range(num):
    distances[z][z] = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == z+1:
                iDistance(i,j,z+1)
result = 987654321
for z in range(num):
    visit = [0] * num
    visit[z] = 1
    check(1,z,0,visit)

# print()
# for val in arr:
#     print(val)
# for val in distances:
#     print(val)

if result == 987654321:
    print(-1)
else:
    print(result)