def dfs(r,c):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visited = [[0] * L for _ in range(L)]
    stack = list()
    stack.append((r,c))
    # while stack: # 스택이 비어있지 않다면 계속반복
    #     cr,cc = stack.pop()
    #     visited[cr][cc] = 1
    #     for d in range(4):
    #         nr = cr + dr[d]
    #         nc = cc + dc[d]
    #         #범위내에 있고, 방문안했고, 통로여야 됨
    #         if 0<= nr < L and 0<= nc < L and not visited[nr][nc] and maze[nr][nc] ==0:
    #             stack.append((nr,nc))
    #         elif maze[nr][nc] == 3:
    #             return 1

    while stack: # 스택이 비어있지 않다면 계속반복
        cr,cc = stack[-1]
        visited[cr][cc] = 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            #범위내에 있고, 방문안했고, 통로여야 됨
            if 0<= nr < L and 0<= nc < L and not visited[nr][nc] and maze[nr][nc] ==0:
                stack.append((nr,nc))
                break
            elif maze[nr][nc] == 3:
                return 1
        else:   # for문에서 break가 안걸렸다면, 길이 없음.
            #현재노드(stack의 top) 더 이상 검사할 필요없음
            stack.pop()
    return 0


#DFS : 반복문 / 재귀
T = 10
for t in range(T):
    tc = input()
    L = 16
    maze = [list(map(int,input())) for _ in range(L)]
    result = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                result = dfs(i,j)
                break
    print("#{} {}".format(tc,result))


#재귀
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if maze[nr][nc] == 3:
            return 1
        if 0<= nr <L and 0<=nc <L and not visited[nr][nc] and not maze[nr][nc]:
            if dfs(nr,nc):  #다음 단계에서 경로를 찾았으면, 다른 경로는 찾을 필요없음
                return 1
    return 0

#DFS : 재귀
T = 10
for t in range(T):
    tc = input()
    L = 16
    maze = [list(map(int,input())) for _ in range(L)]
    visited = [[0]*16 for _ in range(L)]
    result = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                result = dfs(i,j)
                break
    print("#{} {}".format(tc,result))