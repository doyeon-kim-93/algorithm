def make_set(x):
    Parent[x] = x

def find_set(x):
    if Parent[x] == x :
        return x
    else:
       Parent[x] = find_set(Parent[x])
    return Parent[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        Parent[py] = px
    else:
        Parent[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

T = int(input())
for tc in range(1, 1 + T):
    V, E= map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    edges.sort(key=lambda x:x[2])
    Parent = [0] * (V+1)
    rank = [0] * (V+1)
    for i in range(V+1):
        make_set(i)
    result = 0
    cnt = 0
    mst = []
    for i in range(E):
        s,e,c = edges[i][0],edges[i][1],edges[i][2]
        if find_set(s) == find_set(e):
            continue
        result += c
        mst.append(edges[i])
        union(s,e)

        cnt += 1
        if cnt == V:
            break
    print('#{} {}'.format(tc,result))