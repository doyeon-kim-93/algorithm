tetromino = [[[0, 1], [0, 2], [0, 3]],
             [[1, 0], [2, 0], [3, 0]],
             [[0, 1], [1, 0], [1, 1]],
             [[1, 0], [2, 0], [2, 1]],
             [[1, 0], [2, 0], [2, -1]],
             [[0, 1], [0, 2], [1, 0]],
             [[0, 1], [0, 2], [1, 2]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 0], [2, 0]],
             [[0, 1], [0, 2], [-1, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[1, 0], [1, 1], [2, 1]],
             [[1, 0], [1, -1], [2, -1]],
             [[0, 1], [-1, 1], [-1, 2]],
             [[0, 1], [1, 1], [1, 2]],
             [[0, 1], [0, 2], [1, 1]],
             [[1, 0], [1, 1], [2, 0]],
             [[1, 0], [1, -1], [2, 0]],
             [[0, 1], [0, 2], [-1, 1]]]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        for z in range(len(tetromino)):
            con = arr[i][j]
            cnt = 0
            for y,x in tetromino[z]:
                nr = i + y
                nc = j + x
                if 0<=nr<N and 0<=nc<M:
                    con += arr[nr][nc]
                    cnt += 1
            if cnt == 3:
                result = max(result,con)
print(result)