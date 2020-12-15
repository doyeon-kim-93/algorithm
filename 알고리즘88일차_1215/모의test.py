import collections

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,-1,1,-1,1,-1,1]

def checkIOT(r,c,ln,num):
        for i in range(8):
            nr, nc = r, c
            while 1:
                nr += dr[i]
                nc += dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if (abs(nr-r)+abs(nc-c)) <= ln:
                        IOTArr[nr][nc] += [num]
                    else:
                        break
                else:
                    break
def check(arr2):
    r,c = arr2
    if len(IOTArr[r][c]) > 0:
        for z in range(len(IOTArr[r][c])):
            IOT[IOTArr[r][c][z]-10] = 1
    for i in range(8):
        nr,nc = r,c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if (abs(nr - r) + abs(nc - c)) <= R:
                    if len(IOTArr[nr][nc]) > 0:
                        for z in range(len(IOTArr[nr][nc])):
                            IOT[IOTArr[nr][nc][z] - 10] = 1
                else:
                    break
            else:
                break

def combPort(idx,cnt,M,n):
    global result,flag,IOT
    if cnt == M:
        for i in range(n):
            if portVisit[i] == 1:
                check(port[i])
        if sum(IOT) == len(IOT):
            flag = True
            result = min(result,M)
        else:
            IOT = [0] * ((IOTIdx - 10))
        return

    if idx >= n:
        return
    portVisit[idx] = 1
    combPort(idx+1,cnt+1,M,n)
    portVisit[idx] = 0
    combPort(idx+1,cnt,M,n)

T = int(input())
for tc in range(1,T+1):
    N,R = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    IOTArr = [[[] for _ in range(N)] for _ in range(N)]
    port = []
    q = collections.deque([])
    IOTIdx = 10
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                port += [(i,j)]
            elif arr[i][j] != 9 and arr[i][j] > 0:
                IOTArr[i][j] += [IOTIdx]
                checkIOT(i,j,arr[i][j],IOTIdx)
                IOTIdx += 1

    result = 987654321
    flag = False
    portVisit = [0] *len(port)
    IOT = [0]*((IOTIdx-10))

    if len(port) > 5:
        for i in range(1,len(port)+1):
            combPort(0,0,i,len(port))
            IOT = [0] * ((IOTIdx - 10))
    else:
        for i in range(1,6):
            combPort(0,0,i,len(port))
            IOT = [0] * ((IOTIdx - 10))

    if flag:
        print('#{} {}'.format(tc,result))
    else:
        print('#{} {}'.format(tc,-1))

