### MST(최소 신장 트리)

> ​	**MST = Minimum Spanning Tree**
>
> ​	간선들이 가중치가 있는 그래프에서 간선 가중치의 합이 가장 작은 트리를 말한다



#### 크루스칼 알고리즘

> 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘, **최소 비용 신장 트리(Minimum Spanning Tree)**를 만들기 위한 대표적인 알고리즘이다. 흔히 여러 개의 도시가 있을 대, 각 도시를 도로를 이용해 최소한의 비용으로 연결하고자 할 때 적용된다.
>
> 핵심 개념은 "간선을 거리가 짧은 순서대로 그래프에 포함"시키는 것이다. 즉, 모든 노드들을 최대한 적은 비용으로 '연결'만 시키면 되기 때문에 모든 간선 정보를 오름차순으로 정렬한 뒤에 비용이 적은 간선부터 그래프에 포함시킨다.

- 탐욕 알고리즘을 기초로 하고 있음.
- 정렬된 순서에 맞게 노드를 그래프에 포함시킨다.
- 포함시키기 전에는 **사이클 테이블**을 확인한다.
- 사이클을 형성하는 경우 간선을 포함하지 않는다.

#### 코드 작성

``` python
parent = dict()
rank = dict()


# vertice 초기화
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
    # print(parent)
    # print(rank)


# 해당 vertice의 최상위 정점을 찾는다
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


# 두 정점을 연결한다
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
    print(rank)


def kruskal(graph):
    minimum_spanning_tree = []

    # 초기화
    for vertice in graph['vertices']:
        make_set(vertice)

    # 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 간선 연결 (사이클 없게)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

print(kruskal(graph))
```



``` python
import sys
input=sys.stdin.readline

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

N,M = map(int,input().split())

arrs = []
for _ in range(M):
    v1,v2,val = map(int,input().split())
    arrs += [(v1,v2,val)]
parents = {}
rank = {}

result = 0
for i in range(N+1):
    make_set(i)

arrs.sort(key=lambda x:x[2])

for arr in arrs:
    v1,v2,val = arr
    if find(v1) != find(v2):
        union(v1,v2)
        result += val
print(result)

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
```



