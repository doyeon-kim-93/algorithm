import collections
dr = [1,-1,0,0,-1,-1,1,1]
dc = [0,0,1,-1,-1,1,-1,1]
def bfs():
    global cnt,Q
    while Q :
        r,c = Q.popleft()
        for z in range(8):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<10 and 0<=nc<10 and arr[nr][nc] == 1:
                arr[nr][nc] = cnt
                Q += [(nr,nc)]
T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(10)]
    Q = collections.deque([])
    cnt = 1
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = cnt
                Q += [(i,j)]
                bfs()
    print('#{} {}'.format(tc,cnt-1))