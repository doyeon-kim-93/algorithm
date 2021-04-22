import sys
sys.stdin = open("input.txt", "r")
def checkMax(idx,cnt,honey,a):
    global C,hVisit,man1,man2
    if idx == len(honey):
        con = 0
        for z,val in enumerate(hVisit):
            if val == 1:
                con += honey[z]
        if con <= C:
            con = 0
            for z, val in enumerate(hVisit):
                if val == 1:
                    con += (honey[z]*honey[z])
        else:
            return
        if a == 1:
            man1 = max(man1,con)
        else:
            man2 = max(man2,con)
        return
    hVisit[idx] = 1
    checkMax(idx+1,cnt+1,honey,a)
    hVisit[idx] = 0
    checkMax(idx+1, cnt, honey, a)

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    hVisit = [0]*M
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            man1 = -1
            point = []
            honey1 = []
            r,c, = i,j
            for z in range(M):
                nc = c + z
                if 0 <= r < N and 0 <= nc < N:
                    honey1 += [arr[r][nc]]
                    visit[r][nc] = 1
                    point += [(r,nc)]
            checkMax(0,0,honey1,1)
            for y in range(N):
                for x in range(N-M+1):
                    flag = True
                    if visit[y][x] == 0:
                        man2 = -1
                        point2 = []
                        honey2 = []
                        for t in range(M):
                            nx = x + t
                            if 0<=x<N and 0<=y<N and visit[y][nx] == 0:
                                honey2 += [arr[y][nx]]
                                visit[y][nx] = 1
                                point2 += [(y, nx)]
                            else:
                                flag = False
                                break
                        if flag and len(honey2) == M:
                            checkMax(0,0,honey2,2)
                            result = max(result,(man1+man2))
                        for n,m in point2:
                            visit[n][m] = 0
            for y,x in point:
                visit[y][x] = 0
    print('#{} {}'.format(tc,result))