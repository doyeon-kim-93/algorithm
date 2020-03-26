import copy
def check(k,start):
    global N,M,arrow,li_arrow
    if k == 3:
        a = copy.deepcopy(arrow)
        li_arrow += [a]
        return
    else:
        for z in range(start,M):
            arrow += [[N,z]]
            check(k+1,z+1)
            arrow.pop()

N, M, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr += [[0] * M]
enemy = []
for i in range(N-1,-1,-1):
    for j in range(M):
        if arr[i][j] == 1:
            enemy += [[i,j]]
cnt = len(enemy)
li_arrow = []
arrow = []
check(0,0)
result = -1
for i in range(len(li_arrow)):
    re_enemy = copy.deepcopy(enemy)
    visit = [0] * cnt
    n = copy.deepcopy(cnt)
    con = 0
    while n>0 :
        for j in range(3):
            lens = 30
            po = 30
            t = 30
            flag = False
            for z in range(cnt):
                if re_enemy[z][0] >= N :
                    n -= 1
                    re_enemy[z][0] = -1
                    re_enemy[z][1] = -1
                elif re_enemy[z][0] >= 0 and re_enemy[z][1] >= 0 :
                    if (abs(li_arrow[i][j][0] - re_enemy[z][0]) + abs(li_arrow[i][j][1] - re_enemy[z][1])) <= D:
                        flag = True
                        p = (abs(li_arrow[i][j][0] - re_enemy[z][0]) + abs(li_arrow[i][j][1] - re_enemy[z][1]))
                        if p < lens:
                            lens = p
                            po = re_enemy[z][1]
                            t = z
                        elif p == lens:
                            po = min(po,re_enemy[z][1])
                            if po == re_enemy[z][1]:
                                t = z
            if flag:
                visit[t] += 1
        for x in range(cnt):
            if visit[x] > 0:
                re_enemy[x][0] = -1
                re_enemy[x][1] = -1
                n -= 1
                con += 1
                visit[x] = 0
            else:
                re_enemy[x][0] += 1
    result = max(result,con)
print(result)