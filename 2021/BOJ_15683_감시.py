dr = [0,0,-1,1]
dc = [1,-1,0,0]

def scan(k,tmpArr,dir,y,x):
    n = len(cctvList[k][dir])
    for i in range(n):
        r,c = y,x
        z = cctvList[k][dir][i]
        while 1:
            r += dr[z]
            c += dc[z]
            if 0<=r<N and 0<=c<M:
                if tmpArr[r][c] == 6:
                    break
                elif tmpArr[r][c] == 0:
                    tmpArr[r][c] = 9
            else:
                break

def check(cnt,tmpList,lenCCTV):
    global cctv,result,arr,N
    if cnt == lenCCTV:
        tmparr = [arr[i][:] for i in range(N)]
        for z in range(lenCCTV):
            r,c = cctv[z]
            scan(arr[r][c],tmparr,tmpList[z],r,c)
        con = 0
        for i in range(N):
            for j in range(M):
                if tmparr[i][j] == 0:
                    con += 1
        result = min(result,con)
        return
    y,x = cctv[cnt]
    if arr[y][x] == 2:
        for i in range(2):
            tmpList += [i]
            check(cnt + 1, tmpList, lenCCTV)
            tmpList.pop()
    else:
        for i in range(4):
            tmpList += [i]
            check(cnt + 1, tmpList, lenCCTV)
            tmpList.pop()

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
cctv5 = []
cctvList = [[],[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,2],[0,3],[1,3],[1,2]],[[0,1,2],[0,2,3],[0,1,3],[1,2,3]]]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            if arr[i][j] == 5:
                cctv5 += [(i,j)]
            else:
                cctv += [(i,j)]
for i,j in cctv5:
    for z in range(4):
        r = i
        c = j
        while 1:
            r += dr[z]
            c += dc[z]
            if 0<=r<N and 0<=c<M:
                if arr[r][c] == 6:
                    break
                elif arr[r][c] == 0:
                    arr[r][c] = 9
            else:
                break
result = 987654321
check(0,[],len(cctv))
print(result)
