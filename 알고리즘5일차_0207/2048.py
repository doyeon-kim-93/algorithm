T = int(input())
for tc in range(1,T+1):
    n, direction = map(str, input().split())
    N =int(n)
    arr = [list(map(int, input().split())) for _ in range(N)]
    def go(direction):
        if direction == 'left':
            for i in range(N):
                for j in range(N):
                    if j != N - 1:
                        if arr[i][j] == arr[i][j+1]:
                            arr[i][j]=(arr[i][j])*2
                            arr[i][j+1]= 0

            for _ in range(N//2):
                for i in range(N):
                    for j in range(N):
                        if j != N-1:
                            if arr[i][j] == 0:
                                arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]

        if direction == 'right':
            for i in range(N):
                for j in range(-1,-1,-1):
                    if j != 0:
                        if arr[i][j] == arr[i][j+1]:
                            arr[i][j]=(arr[i][j])*2
                            arr[i][j+1]= 0

            for _ in range(N//2):
                for i in range(N):
                    for j in range(-1,-1,-1):
                        if j != 0:
                            if arr[i][j] == 0:
                                arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
        if direction == 'up':
            for i in range(N):
                for j in range(N):
                    if i != N - 1:
                        if arr[j][i] == arr[j][i+1]:
                            arr[j][i]=(arr[j][i])*2
                            arr[j][i+1]= 0

            for _ in range(N//2):
                for i in range(N):
                    for j in range(N):
                        if i != N-1:
                            if arr[j][i] == 0:
                                arr[j][i],arr[j][i+1] = arr[j][i+1],arr[j][i]
        if direction == 'down':
            for i in range(N - 1, -1, -1):
                for j in range(N - 1, -1, -1):
                    if j != 0:
                        if arr[j][i] == arr[j - 1][i]:
                            arr[j][i] = (arr[j][i]) * 2
                            arr[j - 1][i] = 0

            for _ in range(N // 2):
                for i in range(N - 1, -1, -1):
                    for j in range(N - 1, -1, -1):
                        if j != 0:
                            if arr[j][i] == 0:
                                arr[j][i], arr[j - 1][i] = arr[j - 1][i], arr[j][i]

        return arr
    result = go(direction)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()