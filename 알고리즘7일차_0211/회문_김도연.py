# import sys
# sys.stdin = open("sample_input (4)", "r")
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    result_list = []
    #가로탐색
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            k = 0
            for z in range(M):
                if arr[i][j+z] == arr[i][(j+M)-1-z]:
                    cnt += 1
                    k = j
                else:
                    cnt = 0
            if cnt == M:
                result = ''
                for z in range(M):
                    result += arr[i][k+z]
                result_list.append(result)
    #세로탐색
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            k = 0
            for z in range(M):
                if arr[j+z][i] == arr[(j+M)-1-z][i]:
                    cnt += 1
                    k = j
                else:
                    cnt = 0
            if cnt == M:
                result = ''
                for z in range(M):
                    result += arr[k+z][i]
                result_list.append(result)
    print('#{}'.format(tc),end = ' ')
    for i in range(len(result_list)):
        print(result_list[i])