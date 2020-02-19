import sys
sys.stdin = open("input (1).txt", "r")

dc = [-1, 1]
def dir(r, c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if arr[r][nc] == 1:
            return i
    return 2


def go(st):
    col = st
    for i in range(99,-1,-1):
        if dir(i, col) < 2:
            while 1:
                nc = col + dc[dir(i, col)]
                if nc < 0 or nc >= 100 or arr[i][nc] == 0:
                    break
                col = nc
    return col


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for x in range(len(arr)):
        if arr[99][x] == 2:
            print('#{} {}'.format(tc,go(x)))