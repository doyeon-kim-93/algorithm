N = int(input())
pira = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = pira[0][0]
for i in range(N):
    for j in range(i+1):
        dp[i][j] = pira[i][j] + max(dp[i-1][j],dp[i-1][j-1])
print(max(dp[N-1]))