T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = set()
    for i in range(1 << N):
        con = 0
        for j in range(N):
            if i & (1 << j):
                con += arr[j]
        result.add(con)
    print('#{} {}'.format(tc,len(result)))