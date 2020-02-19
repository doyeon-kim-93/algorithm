def attack(r, c):
    sum = 0
    for i in range(r, r + M):
        for j in range(c, c + M):
            sum += fly[i][j]
    return sum


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 시작위치를 위한 2중 for문
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 파리퇴치를 위한 이중포문
            tmp = attack(i, j)
            if ans < tmp:
                ans = tmp

    print("#{} {}".format(tc, ans))