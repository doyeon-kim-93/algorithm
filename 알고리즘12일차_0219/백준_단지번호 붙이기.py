dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(r,c):
    con = []
    for z in range(4):
        nr = r + dr[z]
        nc = c + dc[z]
        if 0 <= nr < N and 0 <= nc < N:
            con.append(arr[nr][nc])
    if sum(con) == 0:
        arr[r][c] = cnt
        apart_dic[cnt] += 1
    else:
        for z in range(4):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = cnt
                    apart_dic[cnt] += 1
                    dfs(nr,nc)

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

apart_dic = {}
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            apart_dic[cnt] = 0
            dfs(i,j)
result = []
for i in apart_dic.values():
    result.append(i)
k = sorted(result)
print(cnt-1)
for i in range(len(k)):
    print(k[i])