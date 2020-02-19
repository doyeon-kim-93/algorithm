T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_result = 987654321

    for m in range(N):
        for n in range(N):
            sum1 = 0
            sum2 = 0
            sum3 = 0
            for i in range(m):
                for j in range(n):
                    sum1 += arr[i][j]
            for i in range(m,N):
                for j in range(n):
                    sum2 += arr[i][j]
            for i in range(N):
                for j in range(n,N):
                    sum3 += arr[i][j]
            li = [sum1, sum2, sum3]
            result = max(li) - min(li)
            if min_result > result:
                min_result = result
    print('#{} {}'.format(tc,min_result))