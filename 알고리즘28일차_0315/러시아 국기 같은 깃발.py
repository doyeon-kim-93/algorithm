T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    min_cnt = N*M
    for i in range(N-2):
        for j in range(i+1,N-1):
            cnt = 0
            for t in range(i+1):
                for z in range(M):
                    if flag[t][z] != 'W':
                        cnt += 1
            for t in range(i + 1,j+1):
                for z in range(M):
                    if flag[t][z] != 'B':
                        cnt += 1
            for t in range(j+1,N):
                for z in range(M):
                    if flag[t][z] != 'R':
                        cnt += 1
            min_cnt = min(min_cnt,cnt)
    print('#{} {}'.format(tc,min_cnt))