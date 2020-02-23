def start(k):
    if k == M :
        print(' '.join(map(str, result)))
        return
    che = 0
    for i in range(N):
        if not visit[i] and che != arr[i]:
            visit[i] = 1
            result.append(arr[i])
            che = arr[i]
            start(k+1)
            visit[i] = 0
            result.pop()

N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visit = [0]*N
result = []
start(0)
