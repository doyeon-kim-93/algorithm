# import sys
# sys.stdin = open("input.txt", "r")
dr = [0,0]
dc = [-1,1]

def move():
    global arr,flag2
    for z in range(N):
        r,c = 0,z
        while 1:
            if r == H and c == z:
                break
            elif r == H and c != z:
                return False
            if arr[r][c] == 1:
                nr = r + 1
                nc = c - 1
                if 0<=nr<H+1 and 0<=nc<N:
                    r,c = nr,nc
            elif arr[r][c] == 0:
                flag = True
                if c+1 < N and arr[r][c+1] == 1:
                    c += 1
                    r += 1
                    flag = False
                if flag:
                    r += 1
    flag2 = True
    return

def check(idx,cnt,k):
    global arr,result,visit,posible
    if cnt == k:
        tmp = []
        for i in range(len(visit)):
            if visit[i] == 1:
                tmp += [posible[i]]
        for r,c in tmp:
            for z in range(2):
                nr = r + dr[z]
                nc = c + dc[z]
                if 0<=nr<H and 0<=nc<N:
                    if [nr,nc] in tmp:
                        return
        for y,x in tmp:
            arr[y][x] = 1
        move()
        for y,x in tmp:
            arr[y][x] = 0
        return
    if idx >= len(visit):
        return
    visit[idx] = 1
    check(idx+1, cnt+1, k)
    visit[idx] = 0
    check(idx + 1, cnt, k)

N,M,H = map(int,input().split())
sadari = []
if M:
    sadariInput = [list(map(int,input().split())) for _ in range(M)]
    for r,c, in sadariInput:
        sadari += [[r-1,c]]
arr = [[0]*N for _ in range(H+1)]
for r,c in sadari:
    arr[r][c] = 1
posible = []
for i in range(H):
    for j in range(1,N):
        if arr[i][j] == 0:
            cnt = 0
            for z in range(2):
                nr = i + dr[z]
                nc = j + dc[z]
                if 0<=nr<H and 0<=nc<N:
                    if arr[nr][nc] == 1:
                        cnt += 1
            if not cnt:
                posible += [[i,j]]
visit = [0]*len(posible)
result = -1
flag2 = False
for i in range(4):
    check(0,0,i)
    if flag2:
        result = i
        break
print(result)
