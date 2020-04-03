N = int(input())
wine = [0]
for _ in range(N):
    wine += list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(N+1):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = wine[1]
    elif i == 2:
        dp[2] = wine[1]+wine[2]
    else:
        dp[i] = max(dp[i-1],wine[i]+dp[i-2],wine[i]+wine[i-1]+dp[i-3])
print(dp[N])