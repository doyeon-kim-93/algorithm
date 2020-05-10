def chek():
    global result
    while 1 :
        for i in range(N):
            if arr[i][0] < result[-1][-1] and visit[i] == 0:
                visit[i] = 1
        if not 0 in visit:
            return
        point = 987654321
        inx = 0
        for i in range(N):
            if visit[i] == 0 and arr[i][0] >= result[-1][-1] and arr[i][1] < point:
                visit[i] = 1
                inx = i
                point = arr[i][1]
        result += [arr[inx]]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
    visit = [0] * N
    visit[0] = 1
    result = [arr[0]]
    chek()
    print('#{} {}'.format(tc,len(result)))
