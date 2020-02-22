def Qeen(r):
    global result_cnt
    if r == N:
        result_cnt +=1
        return
    else:
        for i in range(N):
            if visit[i] == 0:
                flag = True
                for n in range(r):
                    for m in range(N):
                        if abs(r-n) == abs(i-m):
                            if arr[n][m] == 1:
                                flag = False
                                break
                if flag:
                    arr[r][i] = 1
                    visit[i] = 1
                    Qeen(r+1)
                    arr[r][i] = 0
                    visit[i] = 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    visit = [0]*N
    result_cnt = 0
    Qeen(0)
    print('#{} {}'.format(tc,result_cnt))