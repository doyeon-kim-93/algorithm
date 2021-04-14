import sys
input = sys.stdin.readline

def move(dr,r, c, N):
    global result
    if r == N-1 and c == N-1:
        result += 1
        return
    if dr == 1 or dr == 3 :
        if 0 <= c + 1 < N:
            if arr[r][c + 1] == 0:
                move(1,r, c+1, N)
    if dr == 2 or dr == 3:
        if 0 <= r + 1 < N:
            if arr[r + 1][c] == 0:
                move(2, r+1, c, N)
    if dr == 1 or dr == 2 or dr == 3:
        if 0 <= r + 1 < N and 0 <= c + 1 < N:
            if arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
                move(3, r+1, c + 1, N)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
move(1, 0, 1, N)
print(result)
