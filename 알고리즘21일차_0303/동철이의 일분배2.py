import sys
sys.stdin = open("input (5).txt", "r")

def check(k,n):
    global result
    if n <= result:
        return
    if k == N:
        if result < n:
            result = n
        return
    else:
        for z in range(N):
            if visit[z] == 0:
                visit[z] = 1
                check(k+1,n * work[k][z])
                visit[z] = 0
def div(x):
    return int(x) * 0.01

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work = [list(map(div,input().split())) for _ in range(N)]
    visit = [0] * N
    result = -1
    check(0,1)
    result *= 100
    print('#{}'.format(tc),end = ' ')
    print('{0:0.6f}'.format(result))