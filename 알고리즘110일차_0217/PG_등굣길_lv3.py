def solution(m, n, puddles):
    dp = [[1] * m for _i in range(n)]

    for x, y in puddles:
        dp[y - 1][x - 1] = 0
        if x - 1 == 0:
            for k in range(y - 1, n):
                dp[k][0] = 0
        if y - 1 == 0:
            for k in range(x - 1, m):
                dp[0][k] = 0

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    answer = dp[n - 1][m - 1]
    return answer % 1000000007

# //시간초과
dr = [0,1]
dc = [1,0]
from collections import deque
def solution(m, n, puddles):
    arr = [[-1]*m for _ in range(n)]
    for i,j in puddles:
        arr[j-1][i-1] = 9998
    arr[0][0] = 0
    arr[n-1][m-1] = 9999
    q = deque([])
    q += [(0,0)]
    result = []
    while q:
        r,c = q.popleft()
        for z in range(2):
            nr = r + dr[z]
            nc = c + dc[z]
            if 0<=nr<n and 0<=nc<m :
                if arr[nr][nc] < 0:
                    arr[nr][nc] = arr[r][c] + 1
                    q += [(nr,nc)]
                elif arr[nr][nc] != 9998 and arr[nr][nc] != 9999 and arr[r][c] < arr[nr][nc]:
                    arr[nr][nc] = arr[r][c] + 1
                    q += [(nr,nc)]
                elif arr[nr][nc] == 9999:
                    result += [arr[r][c]]
    if result:
        minVal = min(result)
        cnt = result.count(minVal)
    else:
        cnt = 0
    answer = cnt % 1000000007
    return answer

print(solution(4,3,[[2,2]]))
