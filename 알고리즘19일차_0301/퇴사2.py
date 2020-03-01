def check(n,k):
    global result
    if 0 <= n + work[n][0] < N :
        check(n+work[n][0], k+work[n][1])
    else:
        if result < k:
            result = k
            return
N = int(input())
work = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N):
    if 0 <= i + work[i][0] < N:
        check(i,work[i][1])
print(result)