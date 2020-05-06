dr = [1,0]
dc = [0,1]

def chek(r,c,k):
    global result
    if r == N-1 and c == N-1:
        result = min(result,k)
        return
    elif k >= result:
        return
    else:
        for z in range(2):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                k += arr[nr][nc]
                chek(nr,nc,k)
                visit[nr][nc] = 0
                k -= arr[nr][nc]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    result = 0xfffffff
    visit[0][0] = 1
    chek(0,0,arr[0][0])
    print('#{} {}'.format(tc,result))