import sys
sys.stdin = open("input.txt", "r")
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(r,c,H,f,cost):
    global visit,result,k
    cnt = 0
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
            if arr[nr][nc] < H:
                visit[nr][nc] = 1
                check(nr,nc,arr[nr][nc],f,cost+1)
                visit[nr][nc] = 0
            else:
                if f:
                    cnt2 = 0
                    for i in range(1,k+1):
                        if arr[nr][nc]-i < arr[r][c] and visit[nr][nc] == 0:
                            visit[nr][nc] = 1
                            check(nr, nc,arr[nr][nc]-i, 0, cost + 1)
                            visit[nr][nc] = 0
                        else:
                            cnt2 += 1
                    if cnt2 == k:
                        cnt += 1
                else:
                    cnt += 1
        else:
            cnt += 1
    if cnt == 4:
        result = max(result,cost)
        return
T = int(input())
def high(k):
    global highM
    highM = max(highM,int(k))
    return int(k)
for tc in range(1,T+1):
    highM = -1
    N,k = map(int,input().split())
    arr = [list(map(high,input().split())) for _ in range(N)]
    highList = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == highM:
                highList += [(i,j)]
    result = -1
    visit = [[0] * N for _ in range(N)]
    for r,c in highList:
        visit[r][c] = 1
        check(r,c,arr[r][c],1,1)
        visit[r][c] = 0
    print('#{} {}'.format(tc,result))