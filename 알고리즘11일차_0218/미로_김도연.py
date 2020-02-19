dr = [1,-1,0,0]
dc = [0,0,1,-1]
def dfs(r,c):
    result.append(arr[r][c])
    arr[r][c] = '.'
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= N-1 and 0 <= nc <= N-1 :
            if arr[nr][nc] == 0:
                dfs(nr,nc)
            elif arr[nr][nc] == 3:
                result.append(3)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                dfs(i,j)
                break
    if 3 in result:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))