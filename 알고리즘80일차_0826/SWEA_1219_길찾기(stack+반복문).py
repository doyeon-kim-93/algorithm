import sys
sys.stdin = open("input.txt","r")

def dfs():
    global adj,visited
    stack = list()
    stack.append(0)

    while stack:
        v = stack.pop() #가장 최근에 추가된 정점 가져오기
        visited[v] = 1
        # 정점에서 갈 수 있는 모든 경로 진행
        if adj[0][v] == 99 or adj[1][v] == 99:
            return 1
        # for i in range(2):
        #     if not visited[adj[i][v]]:  # 다음경로를 방문하지 않았다면, stack에 추가
        #         stack.append(adj[i][v])

        if not visited[adj[0][v]]: # 다음경로를 방문하지 않았다면, stack에 추가
            stack.append(adj[0][v])
        if not visited[adj[1][v]]:
            stack.append(adj[1][v])
    return 0


T = 10
for _ in range(T):
    tc, N = map(int,input().split())
    result = 0
    path = list(map(int,input().split()))
    # 그래프 탐색할 때는 그래프의 노드간 연결정보를 알아야함
    # 보통 인접행렬이나 인접리스트를 통해서 표현한다.
    adj = [[0] * 100 for _ in range(2)]
    visited = [0] * 100
    # 인접행렬에 지점간 연결정보 넣기
    #  0  1  2  3
    # [3][ ][ ][ ]
    # [ ][ ][ ][ ]
    for i in range(0,len(path),2):
        if adj[0][path[i]] == 0:
            adj[0][path[i]] = path[i+1]
        else:
            adj[1][path[i]] = path[i+1]
    result = dfs()
    print("#{} {}".format(tc,result))
