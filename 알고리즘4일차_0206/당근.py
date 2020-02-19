T = int(input())
for tc in range(1,T+1):
    N = int(input())
    carrot = list(map(int,input().split()))
    result = []
    for i in range(N-1):
        sum1 = 0
        sum2 = 0
        for j in range(i+1):
            sum1 += carrot[j]
        for z in range(i+1,N):
            sum2 += carrot[z]
        result.append(abs(sum1-sum2))
    result2 = min(result)
    idx=result.index(result2)
    print(idx+1, result2)