dc = [-1, 1]


def dir_check(r, c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if ladder[r][nc] == 1:
            return i
    return 2


def go(st):
    cnt = 0
    col = st
    for i in range(100):
        dir = dir_check(i, col)
        if dir < 2:
            while 1:
                nc = col + dc[dir]
                if nc < 0 or nc >= 100 or ladder[i][nc] == 0:
                    break
                cnt += 1
                col = nc

        cnt += 1
    return cnt


for tc in range(10):
    tc_num = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_value = 987654321
    ans_idx = 987654321

    for i in range(len(ladder[0])):
        if ladder[0][i] == 1:
            tmp = go(i)
            if tmp <= min_value:
                min_value = tmp
                ans_idx = i

    print("#{} {}".format(tc_num, ans_idx))