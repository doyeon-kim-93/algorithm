dr = [1,-1,0,0]
dc = [0,0,1,-1]
def check(n,m,M):
    global cnt
    for j in range(4):
        nr = n + dr[j]
        nc = m + dc[j]
        if 0<=nr<M and 0<=nc<M and room[nr][nc] - room[n][m] == 1 :
            cnt += 1
            check(nr,nc,M)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    result = [0,0,0]
    for i in range(N):
        for j in range(N):
            cnt = 1
            check(i,j,N)
            if cnt > result[0]:
                result[0] = cnt
                result[1] = i
                result[2] = j
            elif cnt == result[0]:
                if room[i][j] < room[result[1]][result[2]]:
                    result[0] = cnt
                    result[1] = i
                    result[2] = j
    print("#{}".format(tc),end = ' ')
    print(room[result[1]][result[2]],result[0])