import sys
sys.stdin = open("input.txt", "r")

dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]
rever = [0,2,1,4,3]

T = int(input())
for tc in range(1,T+1):
    N,t,K = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    bug = []
    result = 0
    for _ in range(K):
        i,j,val,d = map(int,input().split())
        result += val
        bug += [[i,j,val,d]]
    while t:
        tmp = [[[] for _ in range(N)] for _ in range(N)]
        t -= 1
        if bug:
            for _ in range(len(bug)):
                r,c,val,d = bug.pop(0)
                nr = r + dr[d]
                nc = c + dc[d]
                if 0<=nr<N and 0<=nc<N:
                    if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                        dir = rever[d]
                        nval = val//2
                        kill = val - nval
                        result -= kill
                        if nval != 0:
                            tmp[nr][nc] += [[nr,nc,nval,dir]]
                    else:
                        tmp[nr][nc] += [[nr,nc,val,d]]
            for i in range(N):
                for j in range(N):
                    if len(tmp[i][j]) > 1:
                        con = 0
                        for z in range(len(tmp[i][j])):
                            con += tmp[i][j][z][2]
                        tmp[i][j].sort(key= lambda x: x[2])
                        bug += [[i,j,con,tmp[i][j][-1][-1]]]
                    elif len(tmp[i][j]) == 1:
                        bug += [tmp[i][j][0]]
    print('#{} {}'.format(tc,result))