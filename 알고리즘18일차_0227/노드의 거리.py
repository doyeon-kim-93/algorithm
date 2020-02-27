def bfs(s,f):
    global cnt
    visit[s] = 1
    Q.append(s)
    while Q:
        k = Q.pop(0)
        if k != f:
            for i in range(V+1):
                if node[k][i]==1 and visit[i] != 1 :
                    visit[i] = 1
                    Q.append(i)
                    count_node[i] = count_node[k] + 1
        else:
            cnt = count_node[k]
T = int(input())
for tc in range(1,T+1):
    V, E =map(int,input().split())
    node = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1,n2 = map(int,input().split())
        node[n1][n2]  = node[n2][n1] = 1
    start_node,finish_node = map(int,input().split())
    visit = [0]*(V+1)
    count_node = [0]*(V+1)
    Q = []
    cnt = 0
    bfs(start_node,finish_node)
    print('#{} {}'.format(tc,cnt))