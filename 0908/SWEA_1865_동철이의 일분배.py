import sys
sys.stdin = open("input.txt", "r")
from sys import stdin
input = stdin.readline

def bfs(cnt,result2):
    global result,N
    if cnt == N:
        result = max(result2,result)
        return
    elif result2 <= result:
        return
    else:
        for i in range(N):
            if visit[i] == 0 and  arr[cnt][i] != 0:
                visit[i] = 1
                bfs(cnt+1,result2*arr[cnt][i])
                visit[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(float,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = ((arr[i][j])*0.01)
    visit = [0]*N
    result = 0
    bfs(0,1)
    print("#%d %0.6f" %(tc,round(result*100,6)))
