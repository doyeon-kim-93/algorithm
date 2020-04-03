N = int(input())
num = list(map(int,input().split()))
dp = [0] * (N+1)
result = -987654321
for i in range(N+1):
    if i == 0:
        dp[0] = 0
    else:
        dp[i] = max(num[i-1],num[i-1]+dp[i-1])
        result = max(result,dp[i])

print(result)