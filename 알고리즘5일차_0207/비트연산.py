T = int(input())
for tc in range (1,T+1):
    arr = list(map(int,input()))
    N = len(arr)
    board = [0]*N
    cnt = 0
    for i in range(N-1):
        if i == 1 and arr[0] == 1:
            cnt += 1
        if arr[i] == 0 and arr[i+1] == 1:
            cnt += 1
        if arr[i] == 1 and arr[i+1] == 0:
            cnt += 1

    print('#{} {}'.format(tc,cnt))


