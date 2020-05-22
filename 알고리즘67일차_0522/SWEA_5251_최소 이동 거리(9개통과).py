import collections

def bfs():
    global q,result
    while q:
        point, ln = q.popleft()
        if point == N:
            result = min(result,ln)
        else:
            for i in range(0,N+1):
                if arr[point][i] > 0 and visit[point][i] == 0:
                    visit[point][i] = 1
                    q += [(i,ln+arr[point][i])]

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    arr = [[-1]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        arr[s][e] = w
    q = collections.deque([])
    visit = [[0]*(N+1) for _ in range(N+1)]
    result = 987654321
    q += [(0,0)]
    visit[0][0] = 1
    bfs()
    print('#{} {}'.format(tc,result))