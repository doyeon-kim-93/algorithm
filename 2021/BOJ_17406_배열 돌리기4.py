def cicle(rotation,arr):
    for r,c,z in rotation:
        v = (2*z)//2
        sr,sc = (r-z-1,c-z-1)
        er,ec = (r+z-1,c+z-1)
        for i in range(v):
            sy,sx = sr+i,sc+i
            ey,ex = er-i,ec-i
            tmp = []
            y,x = sr+i,sc+i
            cnt = 0
            while 1:
                if y == sy and x == sx:
                    cnt +=1
                if cnt == 2:
                    break
                if y == sy and sx<= x <ex:
                    tmp +=[(y,x+1,arr[y][x])]
                    x += 1
                elif sy<= y <ey and x == ex:
                    tmp +=[(y+1,x,arr[y][x])]
                    y +=1
                elif y == ey and sx< x <=ex:
                    tmp +=[(y,x-1,arr[y][x])]
                    x -= 1
                elif sy< y <=ey and x == sx:
                    tmp +=[(y-1,x,arr[y][x])]
                    y -=1
            for a,b,val in tmp:
                arr[a][b] = val

def check(cnt,rotaion,n):
    global result,arrInput
    if cnt >= n:
        arr = [row[:] for row in arrInput]
        cicle(rotation,arr)
        score = 987654321
        for val in arr:
            score = min(score,sum(val))
        result = min(result,score)
        return
    for z in range(cnt,n):
        rotation[z],rotaion[cnt] = rotation[cnt],rotaion[z]
        check(cnt+1,rotaion,n)
        rotation[z], rotaion[cnt] = rotation[cnt], rotaion[z]

N,M,K = map(int,input().split())
arrInput = [list(map(int,input().split())) for _ in range(N)]
rotation = [list(map(int,input().split())) for _ in range(K)]
result = 987654321
check(0,rotation,K)
print(result)