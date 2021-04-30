parents = dict()
rank = dict()

def make_set(v):
    parents[v] = v
    rank[v] = 0

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]

def union(v1,v2):
    r1,r2 = find(v1),find(v2)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parents[r2] = r1
        else:
            parents[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += 1

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

for i in range(1,N+1):
    make_set(i)

arr.sort(key= lambda x:x[-1])

result = 0

for ar in arr:
    v1,v2,w = ar
    if find(v1) != find(v2):
        union(v1,v2)
        result += w

print(result)