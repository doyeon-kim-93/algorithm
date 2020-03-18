def dfs(t,cnt):
    global result
    for z in range(1,N+1):
        if arr[t][z] == 1 and visit[z] == 0:
            visit[t] = 1
            cnt += 1
            dfs(z,cnt)
            visit[t] = 0
            cnt -= 1
    else:
        result = max(result,cnt)
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        r,c = map(int,input().split())
        arr[r][c] = arr[c][r] = 1
    result = -1
    for i in range(1,N+1):
        visit = [0] * (N + 1)
        dfs(i,1)
    print('#{} {}'.format(tc,result))