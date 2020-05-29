T = int(input())
for tc in range(1, 1 + T):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        n1,n2,w = map(int,input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    INF = float('inf')
    key = [INF] * (V+1)
    parent = [-1] * (V+1)
    mst = [0] * (V+1)
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < (V+1) :
        U = -1
        min = INF
        for i in range((V+1)):
            if not mst[i] and key[i] < min:
                min = key[i]
                U = i
        mst[U] = 1
        result += min
        cnt += 1
        for w in range((V+1)):
            if adj[U][w] > 0 and not mst[w] and key[w] > adj[U][w]:
                key[w] = adj[U][w]
                parent[w] = U
    print('#{} {}'.format(tc,result))
