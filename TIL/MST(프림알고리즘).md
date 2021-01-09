### MST(최소 신장 트리)

> ​	**MST = Minimum Spanning Tree**
>
> ​	간선들이 가중치가 있는 그래프에서 간선 가중치의 합이 가장 작은 트리를 말한다



#### 프림 알고리즘

> 시작 정점을 선택 한 후, 정점에 인접한 간선 중 최소 간선으로 연결된 정점을 선택하고, 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 최소 신장 트리를 확장해 가는 방식

- 탐욕 알고리즘을 기초로 하고 있음.
- 특정 정점에서 시작, 해당 정점에 연결 된 가장 가중치가 작은 간선을 선택, 간선으로 연결된 정점들에 연결된 간선 중에서 가장 가중치가 작은 간선을 택하는 방식으로 MST 를 구함



#### 코드 작성

1. heapq라이브러리 사용 구현

   ``` python
   import heapq
   
   INF = 999
   adj_mat = [[0, 29, INF, INF, INF, 10, INF],
              [29, 0, 16, INF, INF, INF, 15],
              [INF, 16, 0, 12, INF, INF, INF],
              [INF, INF, 12, 0, 22, INF, 18],
              [INF, INF, INF, 22, 0, 27, 25],
              [10, INF, INF, INF, 27, 0, INF],
              [INF, 15, INF, 18, 25, INF, 0]]
   
   N = len(adj_mat)
   G = [[] for _ in range(N)]
   for i in range(N):
       for j in range(N):
           if adj_mat[i][j] != INF:
               G[i] += [(adj_mat[i][j],j)]
   
   distance = [0]*N
   visit = [False] * N
   parent = [None] * N
   q = []
   for val,i in G[0]:
       heapq.heappush(q,(val,i))
   visit[0] = True
   
   def prim(start):
       s = start
       global q
       while q:
           val,v = heapq.heappop(q)
           if not visit[v]:
               visit[v] = True
               distance[v] = val
               for i in G[v]:
                   heapq.heappush(q,i)
               parent[v] = s
               s = v
   prim(1)
   
   print(distance)
   print(sum(distance))
   print(visit)
   print(parent)
   ```



2. heapdict 라이브러리 사용 구현 

   ``` python
from heapdict import heapdict
   
   def prim(graph, start):
       mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
       for node in graph.keys():
           keys[node] = float('inf')
           pi[node] = None
       keys[start], pi[start] = 0, start
   
       while keys:
           current_node, current_key = keys.popitem()
           mst.append([pi[current_node], current_node, current_key])
           total_weight += current_key
           for adjacent, weight in mygraph[current_node].items():
               if adjacent in keys and weight < keys[adjacent]:
                   keys[adjacent] = weight
                   pi[adjacent] = current_node
       return mst, total_weight
   
   mygraph = {
       'A': {'B': 7, 'D': 5},
       'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
       'C': {'B': 8, 'E': 5},
       'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
       'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
       'F': {'D': 6, 'E': 8, 'G': 11},
       'G': {'E': 9, 'F': 11}
   }
   mst, total_weight = prim(mygraph, 'A')
   print ('MST:', mst)
   print ('Total Weight:', total_weight)
   ```
   
   
   
3. heapq라이브러리 사용 구현 X

   ver1.

   ``` python
   def prim(G,S):
       distance[S] = 0
       for _ in range(N):
           idx = -1
           min = INF
           for i in range(N):
               if not visit[i] and distance[i] < min:
                   idx = i
                   min = distance[i]
           visit[idx] = True
           for j,val in G[idx]:
               if not visit[j] and val < distance[j]:
                   distance[j] = val
                   parent[j] = idx
   
   INF = 999
   adj_mat = [[0, 29, INF, INF, INF, 10, INF],
              [29, 0, 16, INF, INF, INF, 15],
              [INF, 16, 0, 12, INF, INF, INF],
              [INF, INF, 12, 0, 22, INF, 18],
              [INF, INF, INF, 22, 0, 27, 25],
              [10, INF, INF, INF, 27, 0, INF],
              [INF, 15, INF, 18, 25, INF, 0]]
   
   N = len(adj_mat)
   G = [[] for _ in range(N)]
   for i in range(N):
       for j in range(N):
           if adj_mat[i][j] != INF:
               G[i] += [(j,adj_mat[i][j])]
   distance = [INF] * N
   visit = [False] * N
   parent = [None] * N
   
   prim(G,0)
   
   print(distance)
   print(sum(distance))
   print(visit)
   print(parent)
   ```

   ver2.

   ``` python
   def get_min_node(node_num):
       v = None
       for i in range(node_num):
           if not visited[i]:
               v = i
               break
       for i in range(node_num):
           if not visited[i] and distances[i] < distances[v]:
               v = i
   
       return v
   
   
   def prim(start, node_num):
       for i in range(node_num):
           visited[i] = False
           distances[i] = INF
   
       distances[start] = 0
       for i in range(node_num):
           node = get_min_node(node_num)
           visited[node] = True 
   
           for j in range(node_num):
               if adj_mat[node][j] != INF:
                   if not visited[j] and adj_mat[node][j] < distances[j]:
                       distances[j] = adj_mat[node][j]
   
   INF = 999
   adj_mat = [[0, 29, INF, INF, INF, 10, INF],
              [29, 0, 16, INF, INF, INF, 15],
              [INF, 16, 0, 12, INF, INF, INF],
              [INF, INF, 12, 0, 22, INF, 18],
              [INF, INF, INF, 22, 0, 27, 25],
              [10, INF, INF, INF, 27, 0, INF],
              [INF, 15, INF, 18, 25, INF, 0]]
   
   node_num = len(adj_mat)
   visited = [False] * node_num
   distances = [INF] * node_num
   
   print(prim(0, node_num))
   print("distances: ", distances)
   print("minimum cost: ", sum(distances))
   ```

   