def arrmin(k):
    global min_
    if sum(arr2) > min_:
        return
    if k == N:
        sum_ = sum(arr2)
        if sum_ < min_:
            min_ = sum_
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                arr2.append(arr[k][i])
                arrmin(k+1)
                arr2.pop()
                visit[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = []
    min_ = 987654321
    visit = [0]*N
    arrmin(0)
    print('#{} {}'.format(tc,min_))
