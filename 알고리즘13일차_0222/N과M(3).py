def start(k):
    if k == M:
        print("{}".format(" ".join(result)))
        return
    else:
        for z in range(N):
            result.append(arr[z])
            start(k+1)
            result.pop()
N, M = map(int,input().split())
arr = []
result = []
for i in range(1,N+1):
    arr.append(str(i))
start(0)
