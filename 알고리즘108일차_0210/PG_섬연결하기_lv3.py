parent = dict()
rank = dict()

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1,v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += 1

def solution(n, costs):
    answer = 0
    tree = []
    for i in range(n):
        make_set(i)
    costs.sort(key=lambda x:x[2])
    for cost in costs:
        v1,v2,w = cost
        if find(v1) != find(v2):
            union(v1,v2)
            tree.append(cost)
    for i in tree:
        answer += i[2]
    return answer