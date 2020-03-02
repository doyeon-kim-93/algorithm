dr = [1,-1,0,0]
dc = [0,0,1,-1]
def check(n,m,M,cnt):
    r = n
    c = m
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0<=nr<M and 0<=nc<M and room[nr][nc] - room[n][m] == 1 :
            cnt +=1
            check(nr,nc,M,cnt)
    if cnt > result[0]:
        result[0] = cnt
        result[1] = n
        result[2] = m
        return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    result = [0,0,0]
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            check(i,j,N,0)
    print(room[result[1]][result[2]],result[0])