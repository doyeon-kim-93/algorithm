T = int(input())
def dfs(visit, v):
    for i in range(1,V+1):
        if arr[v][i] == 1 and i not in visit:
            visit.append(i)
            dfs(visit,i)
    return visit

for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        st, ed = map(int,input().split())
        arr[st][ed]  = 1
    S, G = map(int,input().split())
    if G in dfs([S], S):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))