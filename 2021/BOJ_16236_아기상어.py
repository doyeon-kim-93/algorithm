dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check(y,x,v):
    global N
    answer = []
    q = []
    visit = [[0]*N for _ in range(N)]
    q += [(y,x,0)]
    visit[y][x] = 1
    minval = 987654321
    while q:
        r,c,val = q.pop(0)
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
                if arr[nr][nc] == 0 or arr[nr][nc] == v:
                    visit[nr][nc] = 1
                    q += [(nr,nc,val+1)]
                elif 0< arr[nr][nc] < v:
                    visit[nr][nc] = 1
                    minval = min(minval,val+1)
                    answer += [(nr,nc,val+1)]
    answer2 = []
    for val in answer:
        if minval == val[-1]:
            answer2 += [val]
    return answer2

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
baby = 2
babyR,babyC = 0,0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            babyR, babyC = i, j
            break
cnt = 0
while 1:
    if cnt == baby:
        baby += 1
        cnt = 0
    posible = check(babyR,babyC,baby)
    if posible:
        cnt += 1
        if len(posible) == 1:
            y,x,val = posible[0]
            arr[babyR][babyC] = 0
            arr[y][x] = 9
            babyR,babyC = y,x
            result += val
        else:
            high = 98764321
            tmp = []
            for y,x,val in posible:
                high = min(high,y)
            for fish in posible:
                y,x,val = fish
                if y == high:
                    tmp += [fish]
            if len(tmp) == 1:
                y, x, val = tmp[0]
                arr[babyR][babyC] = 0
                arr[y][x] = 9
                babyR, babyC = y, x
                result += val
            else:
                tmp.sort(key=lambda x: x[1])
                y, x, val = tmp[0]
                arr[babyR][babyC] = 0
                arr[y][x] = 9
                babyR, babyC = y, x
                result += val
    else:
        break
print(result)