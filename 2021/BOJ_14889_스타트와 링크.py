def check(idx,con,m):
    global visit,result
    if con == m:
        teamA = 0
        teamB = 0
        for i,val in enumerate(visit):
            if val == 1:
                for j,v in enumerate(visit):
                    if j != i and v == 1:
                        teamA += arr[i][j]
            else:
                for j,v in enumerate(visit):
                    if j != i and v == 0:
                        teamB += arr[i][j]
        result = min(result,abs(teamA-teamB))
        return
    if idx >= N:
        return
    visit[idx] = 1
    check(idx+1,con+1,m)
    visit[idx] = 0
    check(idx+1,con,m)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = int(N//2)
visit = [0]*N
result = float('inf')
check(0,0,M)
print(result)