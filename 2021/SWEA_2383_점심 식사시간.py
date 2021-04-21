import sys
sys.stdin = open("input.txt", "r")

def select(cnt,n):
    global visit,result,manCnt,arr,ev,man
    if cnt == n:
        walking = []
        ev2 = [[] for _ in range(2)]
        waiting = [[] for _ in range(2)]
        for z,val in enumerate(visit):
            if val == 1:
                walking += [[ev[0][2],abs(man[z][0]-ev[0][0])+abs(man[z][1]-ev[0][1]),0]]
            else:
                walking += [[ev[1][2],abs(man[z][0]-ev[1][0])+abs(man[z][1]-ev[1][1]),1]]
        time = 1
        manCnt2 = len(walking)
        while manCnt2:
            time += 1
            for i,val in enumerate(walking):
                if val:
                    if val[1] > 0:
                        val[1] -= 1
            for i in range(2):
                tmp = []
                for j,val in enumerate(ev2[i]):
                    if val > 0:
                        val = val - 1
                        ev2[i][j] = val
                for val in ev2[i]:
                    if val > 0:
                        tmp += [val]
                    else:
                        manCnt2 -= 1
                ev2[i] = tmp[:]
                if len(ev2[i]) < 3:
                    posible = 3 - len(ev2[i])
                    for z in range(posible):
                        if waiting[i]:
                            k = waiting[i].pop(0)
                            ev2[i] += [k]
            for i,val in enumerate(walking):
                if val[1] == 0:
                    val[1] = -1
                    if len(ev2[val[-1]]) < 3:
                        ev2[val[-1]] += [val[0]]
                    else:
                        waiting[val[-1]] += [val[0]]
        result = min(result,time)
        return
    for i in range(1,3):
        if visit[cnt] == 0:
            visit[cnt] = i
            select(cnt+1,n)
            visit[cnt] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ev = []
    man = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                man += [(i,j)]
            elif arr[i][j] != 0 and arr[i][j] != 1:
                ev += [(i,j,arr[i][j])]
    manCnt = len(man)
    result = float('inf')
    visit = [0]*manCnt
    select(0,manCnt)
    print('#{} {}'.format(tc,result))
