import sys
sys.stdin = open("input (12).txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, word = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        one = 0
        for j in range(N):
            if arr[i][j] == 1:
                one += 1
            elif arr[i][j] == 0:
                if one == word:
                   cnt += 1
                else:
                    one = 0
                one = 0
            if j == N-1 and arr[i][j] == 1:
                if one == word:
                    cnt += 1
    for i in range(N):
        one = 0
        for j in range(N):
            if arr[j][i] == 1:
                one += 1
            elif arr[j][i] == 0:
                if one == word:
                   cnt += 1
                else:
                    one = 0
                one = 0
            if j == N-1 and arr[j][i] == 1:
                if one == word:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))