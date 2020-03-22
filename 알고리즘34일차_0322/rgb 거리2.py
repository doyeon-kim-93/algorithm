def che(k,sum_cost,color):
    global result
    if sum_cost > result:
        return
    if k == N:
        result = min(result,sum_cost)
        return
    else:
        if k == 0:
            che(k+1,sum_cost+cost[k][0][0],cost[k][0][1])
            che(k+1,sum_cost+cost[k][1][0],cost[k][1][1])
            che(k+1,sum_cost+cost[k][2][0],cost[k][2][1])
        else:
            if color == 'r':
                che(k + 1, sum_cost + cost[k][2][0], cost[k][2][1])
                che(k + 1, sum_cost + cost[k][1][0], cost[k][1][1])
            elif color == 'g':
                che(k + 1, sum_cost + cost[k][2][0], cost[k][2][1])
                che(k + 1, sum_cost + cost[k][0][0], cost[k][0][1])
            else:
                che(k + 1, sum_cost + cost[k][1][0], cost[k][1][1])
                che(k + 1, sum_cost + cost[k][0][0], cost[k][0][1])

N = int(input())
cost = [[] for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(3):
        if j == 0:
            cost[i] += [(arr[i][j],'r')]
        elif j == 1:
            cost[i] += [(arr[i][j],'g')]
        elif j == 2:
            cost[i] += [(arr[i][j],'b')]
result = 987654321
che(0,0,0)
print(result)