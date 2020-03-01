def check(n,k):
    global result
    if 0 <= n + work[n][0] < N :
        check(n+work[n][0], k+work[n][1])
    elif n + work[n][0] >= N:
        if result < k:
            result = k
N = int(input())
work = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N):
    check(i,0)
print(result)
