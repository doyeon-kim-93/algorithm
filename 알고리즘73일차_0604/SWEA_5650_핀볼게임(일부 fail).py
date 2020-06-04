import sys
sys.stdin = open("input.txt", "r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]
reverse = [1,0,3,2]

def dir_check(k,block):
    result = 0
    if block == 1:
        if k == 1:
            result = 3
        elif k == 2:
            result = 0
        else:
            result = reverse[k]
    elif block == 2:
        if k == 0:
            result = 3
        elif k == 2:
            result = 1
        else:
            result = reverse[k]
    elif block == 3:
        if k == 0:
            result = 2
        elif k == 3:
            result = 1
        else:
            result = reverse[k]
    elif block == 4:
        if k == 1:
            result = 2
        elif k == 3:
            result = 0
        else:
            result = reverse[k]
    elif block == 5:
        result = reverse[k]
    return result

def wall_check(k,r,c):
    global con
    if k == 0 and r == 0:
        con += 1
        return reverse[k]
    elif k == 1 and r == N-1:
        con += 1
        return reverse[k]
    elif k == 2 and c ==0:
        con += 1
        return reverse[k]
    elif k == 3 and c ==N-1:
        con += 1
        return reverse[k]
    else:
        return k

def holeMove(k,r,c):
    t = k-6
    for z in hole[t]:
        if z  != (r,c):
            return z
def check(r,c,d):
    global con
    dir = d
    a = r
    b = c
    while 1:
        na = a + dr[dir]
        nb = b + dc[dir]
        a = na
        b = nb
        if 0<=na<N and 0<=nb<N:
            if arr[na][nb] == -1:
                return
            elif arr[na][nb] in holenum:
                y,x = holeMove(arr[na][nb],na,nb)
                a = y
                b = x
            elif arr[na][nb] in blocknum:
                dir = dir_check(dir,arr[na][nb])
                con += 1
            elif na == 0 or nb == 0 or na == N-1 or nb == N-1:
                    dir = wall_check(dir,na,nb)
        else:
            return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    hole = [[] for _ in range(5)]
    holenum = [6,7,8,9,10]
    blocknum = [1,2,3,4,5]
    for i in range(N):
        for j in range(N):
            if arr[i][j] in holenum:
                hole[arr[i][j]-6] += [(i,j)]
    # print(hole)
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for z in range(4):
                    con = 0
                    d = z
                    arr[i][j] = -1
                    check(i,j,d)
                    arr[i][j] = 0
                    result = max(result,con)
    print('#{} {}'.format(tc,result))