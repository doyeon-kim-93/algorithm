T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input(.split()))
    board = [[0]*300 for _ in range(300)]
    point = 1
    for i in range(1,300):
        r = i
        c = 1
        for j in range(1,i+1):
            board[r][c] = point
            point += 1
            r -= 1
            c += 1

