for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    home = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                home += [(i,j)]
    for i in range(N):
        for j in range(N):
            cnt = [0] * (N + 2)
            for p, q in home:
                d = abs(i - p) + abs(j - q) + 1
                if d <= N + 1:
                    cnt[d] += 1
            for k in range(1, N + 2):
                cnt[k] += cnt[k - 1]
                if cnt[k] * M >= (k * k + (k - 1) * (k - 1)):
                    result = max(result, cnt[k])
    print('#{} {}'.format(tc, result))