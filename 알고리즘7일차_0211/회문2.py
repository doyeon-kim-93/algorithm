T = 10
for _ in range(1,T+1):
    tc = int(input())
    N = 100
    arr = [list(map(str,input())) for _ in range(100)]
    #가로탐색
    max_len = 0
    for M in range(100):
        for i in range(N):
            for j in range(N-M+1):
                cnt = 0
                for z in range(M):
                    if arr[i][j+z] == arr[i][(j+M)-1-z]:
                        cnt += 1
                    else:
                        cnt = 0
                if cnt == M:
                    if max_len < M:
                        max_len = M
        #세로탐색
        for i in range(N):
            for j in range(N-M+1):
                cnt = 0
                k = 0
                for z in range(M):
                    if arr[j+z][i] == arr[(j+M)-1-z][i]:
                        cnt += 1
                    else:
                        cnt = 0
                if cnt == M:
                    if max_len < M:
                        max_len = M

    print('#{} {}'.format(tc, max_len))