import sys
sys.stdin = open("input (5).txt", "r")

def check(k,n):
    global result
    if k == n:
        con = 1
        for x in range(N):
            con *= work[x][re_li[x]]
        if result < con:
            result = con
        return
    else:
        for z in range(N):
            if visit[z] == 0:
                visit[z] = 1
                re_li.append(M[z])
                check(k+1,n)
                visit[z] = 0
                re_li.pop()
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work = [list(map(int,input().split())) for _ in range(N)]
    visit = [0] * N
    M = []
    for i in range(N):
        M.append(i)
    result = 0
    re_li = []
    check(0,N)
    re = round(result * (100**-(N-1)),6)
    print('{0:0.6f}'.format(re))