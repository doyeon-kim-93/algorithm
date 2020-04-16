def dfs(k):
    global cnt,visit,tree
    for i in range((E+1)+1):
        if tree[k][i] == 1 and visit[i] == 0:
            visit[i] = 1
            cnt += 1
            dfs(i)

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    tree = [[0]*((E+1)+1) for _ in range((E+1)+1)]
    arr = list(map(int,input().split()))
    visit = [0] * ((E+1)+1)
    visit[N] = 1
    for i in range(E):
        j = 2 * i
        a = arr[j]
        b = arr[j+1]
        tree[a][b] = 1
    cnt = 0
    dfs(N)
    print('#{} {}'.format(tc,(cnt+1)))
