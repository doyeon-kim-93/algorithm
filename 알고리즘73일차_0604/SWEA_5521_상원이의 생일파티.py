import sys
sys.stdin = open("input.txt", "r")

def bfs():
    global result
    while q:
        r = q.pop()
        for i in range(N+1):
            if arr[r][i] == 1 and visit[i] == 0:
                visit[i] = 1
                result += 1
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        arr[a][b] = arr[b][a] = 1
    result = 0
    q = []
    visit = [0]*(N+1)
    visit[1] = 1
    for z in range(N+1):
        if arr[1][z] == 1:
            result += 1
            q += [z]
            visit[z] = 1
    bfs()
    print('#{} {}'.format(tc,result))