def rolling(k):
    global dice
    if k == 1: #동쪽
        dice[1][2],dice[1][1],dice[1][0],dice[3][1] = dice[3][1], dice[1][2],dice[1][1],dice[1][0]
    elif k == 2: #서쪽
        dice[1][2],dice[1][1],dice[1][0],dice[3][1] = dice[1][1],dice[1][0],dice[3][1],dice[1][2]
    elif k == 3: #북쪽
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[3][1],dice[0][1],dice[1][1],dice[2][1]
    else: #남쪽
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[1][1],dice[2][1],dice[3][1],dice[0][1]

def move(r,c,k,n,m):
    if k == 1: #동쪽
        nc = c + 1
        if 0<=r<n and 0<=nc<m:
            return r,nc,1
        else:
            return r,c,0
    elif k == 2: #서쪽
        nc = c - 1
        if 0<=r<n and 0<=nc<m:
            return r,nc,1
        else:
            return r,c,0
    elif k == 3: #북쪽
        nr = r - 1
        if 0<=nr<n and 0<=c<m:
            return nr,c,1
        else:
            return r,c,0
    else: #남쪽
        nr = r + 1
        if 0<=nr<n and 0<=c<m:
            return nr,c,1
        else:
            return r,c,0

N,M,x,y,K = map(int,input().split())
arr =  [list(map(int,input().split())) for _ in range(N)]
ordering = list(map(int,input().split()))
result = []
dice = [[0]*3 for _ in range(4)]
for i in range(K):
    x,y,flag = move(x,y,ordering[i],N,M)
    if flag:
        rolling(ordering[i])
        if arr[x][y] == 0:
            arr[x][y] = dice[1][1]
            result += [dice[3][1]]
        else:
            dice[1][1] = arr[x][y]
            arr[x][y] = 0
            result += [dice[3][1]]
for i in result:
    print(i)