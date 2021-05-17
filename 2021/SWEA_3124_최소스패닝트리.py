T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    arrs = []
    for _ in range(M):
        v1, v2, val = map(int, input().split())
        arrs += [(v1, v2, val)]
    def make_set(edge):
        parents[edge] = edge
        rank[edge] = 0


    def find(edge):
        if parents[edge] != edge:
            parents[edge] = find(parents[edge])
        return parents[edge]


    def union(v1, v2):
        r1 = parents[v1]
        r2 = parents[v2]

        if rank[r1] > rank[r2]:
            parents[r2] = parents[r1]
        else:
            parents[r1] = parents[r2]
            if rank[r1] == rank[r2]:
                rank[2] += 1
    parents = {}
    rank = {}

    result = 0
    for i in range(N + 1):
        make_set(i)

    arrs.sort(key=lambda x: x[2])

    for arr in arrs:
        v1, v2, val = arr
        if find(v1) != find(v2):
            union(v1, v2)
            result += val
    print('#{} {}'.format(tc,result))