T = 10
for tc in range(1,T+1):
    N = 8
    M = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    #가로탐색
    con = 0
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            for z in range(M):
                if arr[i][j+z] == arr[i][(j+M)-1-z]:
                    cnt += 1
                else:
                    cnt = 0
            if cnt == M:
                con += 1
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
                con += 1

    print('#{} {}'.format(tc, con))