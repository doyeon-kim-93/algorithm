from collections import deque
def bfs():
    global q, relation, flag, end, result
    while q:
        spot,con = q.popleft()
        for z in range(N + 1):
            if relation[spot][z] == 1:
                if z == end:
                    flag = True
                    result = con + 1
                else:
                    q += [(z,con+1)]
                    relation[spot][z] = relation[z][spot] = 0
N = int(input())
start, end = map(int, input().split())
M = int(input())
relation = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    relation[a][b] = relation[b][a] = 1
q = deque([])
result = 0
flag = False
for i in range(N + 1):
    if relation[start][i] == 1:
        q += [(i,1)]
        relation[start][i] = relation[i][start] = 0
bfs()

if flag:
    print(result)
else:
    print(-1)