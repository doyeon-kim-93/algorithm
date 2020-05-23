import collections
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def chek():
    global result,q
    while q:
        li = q.popleft()
        r = li[0]
        c = li[1]
        cnt = li[2]
        if r == N-1 and c == N-1:
            print(cnt)
            result = min(result,cnt)
        else:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N :
                    if arr[nr][nc] > arr[r][c]:
                        gap = (arr[nr][nc] - arr[r][c])+1
                    else:
                        gap = 1
                    if visit[nr][nc] > visit[r][c] + gap:
                        visit[nr][nc] = visit[r][c] + gap
                        q += [[nr,nc,visit[nr][nc]]]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]
    visit = [[0xffffff]*N for _ in range(N)]
    q = collections.deque([])
    q += [[0,0,0]]
    visit[0][0] = 1
    result = 987654321
    chek()
    print('#{} {}'.format(tc,result-1))