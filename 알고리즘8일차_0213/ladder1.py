import sys
sys.stdin = open("input (1).txt", "r")

dc = [-1, 1]
def dir(r, c):
    for z in range(2):
        nc = c + dc[z]
        if nc < 0 or nc >= 100:
            continue
        if arr[r][nc] == 1:
            return z
    return 2


def go(st):
    col = st
    for i in range(99,-1,-1):
        dir_ = dir(i, col)
        if dir_ < 2:
            while 1:
                nc = col + dc[dir_]
                if nc < 0 or nc >= 100 or arr[i][nc] == 0:
                    break
                col = nc
    return col


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(len(arr)):
        if arr[99][i] == 2:
            print(go(i))