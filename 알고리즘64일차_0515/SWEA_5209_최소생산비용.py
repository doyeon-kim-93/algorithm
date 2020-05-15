def chek(k):
    global result_cost,cost
    if k == N:
        result_cost = min(result_cost,cost)
        return
    elif cost >= result_cost:
        return
    else:
        for j in range(N):
            if factory[j] == 0:
                cost += arr[k][j]
                factory[j] = 1
                chek(k+1)
                cost -= arr[k][j]
                factory[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    factory = [0] * N
    result_cost = 987654321
    cost = 0
    chek(0)
    print('#{} {}'.format(tc,result_cost))
