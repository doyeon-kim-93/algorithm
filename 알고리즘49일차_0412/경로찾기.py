from collections import deque
def bfs():
    global q, codemap, N, end, flag
    while q:
        point,li = q.popleft()
        for z in range(N+1):
            if codemap[point][z] == 1:
                if z == end:
                    li += [z]
                    for t in range(len(li)):
                        if t == len(li)-1 :
                            print(li[t])
                        else:
                            print(li[t],end = ' ')
                    flag = True
                    break
                else:
                    li += [z]
                    q += [(z,li)]
                    codemap[point][z] = 0
                    codemap[z][point] = 0
        if flag:
            break

N, K = map(int,input().split())
code = [list(map(int,input())) for _ in range(N)]
start,end = map(int,input().split())
codemap = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        con = 0
        for z in range(K):
            if code[i][z] != code[j][z]:
                con += 1
        if con == 1:
            codemap[i+1][j+1] = 1
q = deque([])
flag = False
flag2 = False
for i in range(N+1):
    if codemap[start][i] == 1:
        if i == end:
            print(start,end)
            flag2 = True
        else:
            q += [(i,[start,i])]
            codemap[start][i] = 0
            codemap[i][start] = 0
if not flag2:
    bfs()
    if not flag:
        print(-1)