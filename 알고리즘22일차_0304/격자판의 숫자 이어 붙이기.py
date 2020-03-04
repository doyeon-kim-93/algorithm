dr = [0,0,1,-1]
dc = [1,-1,0,0]
def check(r,c,n,empty):
    if n == 7:
        che.add(empty)
        return
    else:
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<= nr < 4 and 0<=nc<4 :
                empty += arr[nr][nc]
                check(nr,nc,n+1,empty)
                empty = empty[0:-1]
T = int(input())
for tc in range(1,T+1):
    arr = [list(map(str,input().split())) for _ in range(4)]
    che = set()
    for i in range(4):
        for j in range(4):
            check(i,j,1,arr[i][j])
    print('#{} {}'.format(tc,len(che)))