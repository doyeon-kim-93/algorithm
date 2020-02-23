def start(k):
    if k == M :
        print(' '.join(map(str,result)))
        return
    else:
        for i in range(N):
            result.append(arr[i])
            start(k+1)
            result.pop()

N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
result = []
start(0)