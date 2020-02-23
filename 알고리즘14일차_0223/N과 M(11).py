def start(k):
    if k == M :
        print(' '.join(map(str, result)))
        return
    che = 0
    for i in range(N):
        if che != arr[i]:
            result.append(arr[i])
            che = arr[i]
            start(k+1)
            result.pop()

N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
result = []
start(0)