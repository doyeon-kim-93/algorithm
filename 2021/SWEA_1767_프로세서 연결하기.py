# import sys
# sys.stdin = open("input.txt", "r")
#1. 연결 해야 할 코어 찾기
#2. 코어별 전선별 좌표 묶음
#3. 조합으로 찾아보기(전선 리스트를 만들어서 중복 값있으면 return)
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def lineCheck(val):
    global line,N
    r,c = val
    tmpLine = []
    for z in range(4):
        nr,nc = r,c
        tmp = []
        flag = False
        while 1:
            nr += dr[z]
            nc += dc[z]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                        flag = True
                        tmp += [(nr, nc)]
                        break
                    tmp += [(nr,nc)]
                elif arr[nr][nc] == 1:
                    break
            else:
                break
        if flag:
            tmpLine += [tmp]
    return tmpLine

def select(idx,con,lineList):
    global result,line,core,concnt
    if idx >= len(line):
        if con > concnt:
            concnt = con
            result = len(lineList)
        elif con == concnt:
            result = min(result,len(lineList))
        return

    for val in line[idx]:
        flag = True
        for z in val:
            if z in lineList:
                select(idx+1,con,lineList)
                flag = False
                break
        if flag:
            lineList += val
            select(idx+1,con+1,lineList)
            for _ in val:
                lineList.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    pass
                else:
                    core += [(i,j)]
    line2 = [[] for _ in range(len(core))]
    for i,val in enumerate(core):
        line2[i] = lineCheck(val)
    line = []
    for val in line2:
        if val:
            line += [val]
    result = 987654321
    concnt = -1
    select(0,0,[])
    if result == 987654321:
        result = 0
    print('#{} {}'.format(tc,result))
    # for val in line:
    #     print(val)