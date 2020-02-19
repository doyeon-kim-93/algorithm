T = int(input())
for tc in range(1,T+1):
    R, C, N = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    board = [[0]*C for i in range(R)]
    for z in range(N):
        for i in range(arr[z][0]-1,arr[z][2]):
            for j in range(arr[z][1]-1,arr[z][3]):
                board[i][j] += 1

    max_con = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > max_con :
                max_con = board[i][j]
    con = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == max_con:
                con += 1
    print('#{} {}'.format(tc,con))

